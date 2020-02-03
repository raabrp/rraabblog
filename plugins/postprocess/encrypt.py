'''
allow password-protection of drafts
'''

import hashlib
import platform
import time
from base64 import b64encode

from bs4 import BeautifulSoup

from pbkdf2 import PBKDF2
from Crypto import Random
from Crypto.Cipher import AES

def encrypt(content_object, plaintext):
    '''
    works by applying side-effects to content_object
    '''

    start = time.time()

    # will not be listed in index
    content_object.status = 'draft'

    # new slug is hash( hash(old_slug) XOR hash(hostname) )
    old_slug = content_object.slug
    hostname = platform.node()
    slug = hashlib.md5(
        b''.join(
            [int.to_bytes(a ^ b, 1, 'little') for (a, b) in zip(
                hashlib.md5(old_slug.encode()).digest(),
                hashlib.md5(platform.node().encode()).digest()
            )])
    ).hexdigest()
    content_object.slug = slug

    # https://github.com/MaxLaumeister/clientside-html-password/blob/master/python/encrypt.py
    plaintext = plaintext + u"""
<script type=text/javascript>
    document.getElementsByTagName("title")[0].innerHTML=("{0}");
    document.getElementById("title-header").innerHTML=("{0}");
    clearToEngage = true;
    setTimeout(engage, 3000);
</script>
""".format(content_object.title)

    salt = Random.new().read(32)
    iv = Random.new().read(16)

    key = PBKDF2(
        passphrase=content_object.password,
        salt=salt,
        iterations=100
    ).read(32)

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        IV=iv
    )

    for i in range(16):
        try:
            encrypted = cipher.encrypt(plaintext)
            break
        except ValueError:
            plaintext += chr(0)

    cryptosoup = BeautifulSoup('''
<div id="contentWrapper">
<p>This draft is password protected before publication.</p>
<input id="pass" type="password" name="pass">
<button id="submitPass" type="button">Submit</button>
<!-- From https://cdnjs.com/libraries/crypto-js -->
<script src="theme/js/lib/cryptojs_aes.js"></script>
<script src="theme/js/lib/cryptojs_pbkdf2.js"></script>
<!--
Code adapted from https://github.com/MaxLaumeister/clientside-html-password
-->
<script type="text/javascript">

    // delays all onReady calls.
    clearToEngage = false;

    var encrypted_content = CryptoJS.enc.Base64.parse("{data}");
    var salt = CryptoJS.enc.Base64.parse("{salt}");
    var iv = CryptoJS.enc.Base64.parse("{iv}");

    var contentWrapper = document.getElementById('contentWrapper');
    var submitPass = document.getElementById('submitPass');
    var passEl = document.getElementById('pass');

    function decrypt() {{
        var password = passEl.value;

        var _cp = CryptoJS.lib.CipherParams.create({{
            ciphertext: encrypted_content
        }});

        var key = CryptoJS.PBKDF2(
            password,
            salt,
            {{
                keySize: 256/32,
                iterations: 100
            }});
        var decrypted = CryptoJS.AES.decrypt(
            _cp,
            key,
            {{
                iv: iv
            }}
        );

        contentWrapper.innerHTML = decrypted.toString(CryptoJS.enc.Utf8);

        // run injected script tags
        recursiveInjectScript(contentWrapper);

    }}

    // run injected scripts
    // https://stackoverflow.com/a/20584396
    function recursiveInjectScript(node) {{
        if (node.tagName === "SCRIPT") {{
            node.parentNode.replaceChild( injectScript(node), node);
        }} else {{
            var i = 0;
            var children = node.childNodes;
            while( i < children.length ) {{
                recursiveInjectScript( children[i++] );
            }}
        }}
    }}

    function injectScript(node) {{
        var script = document.createElement("script");
        script.text = node.innerHTML;
        for( var i = node.attributes.length - 1; i >= 0; i-- ) {{
            script.setAttribute(
                node.attributes[i].name,
                node.attributes[i].value
            );
        }}
        return script;
    }}

    passEl.onkeypress = function(e) {{
        if (!e) e = window.event;
        var keyCode = e.keyCode || e.which;
        if (keyCode == '13') {{
            // Enter pressed
            decrypt();
            return false;
        }}
    }}

    submitPass.onclick = decrypt;

    document.getElementById('pass').focus();

</script>
</div>
'''.format(
    data=b64encode(encrypted).decode("utf-8"),
    salt=b64encode(salt).decode("utf-8"),
    iv=b64encode(iv).decode("utf-8")
),
    'html.parser')

    # title and content
    content_object.title = "[Encrypted]"
    content_object._content = cryptosoup.decode()

    print(round(time.time() - start, 2), "seconds encrypting")
