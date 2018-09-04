/*
 * Built with [Vanilla.js](http://vanilla-js.com/)
 *//*
'''

What happens here:

* Define a function akin to jQuery's `$(document).ready()`

* Unhide links for switching theme.

* mousing over references/footnotes raises content to overlay at
  bottom of screen

* Allow scrolling events to trigger functions when an element starts
  and stops being fully in view.

* Provide a way to have parallel animations running from a single
  `getAnimationFrame` loop.

'''
*/

// all scripts may use onReady rather than window.onload
// to avoid conflict
function onReady(callback) {
    var registered = window.onload;
    if (document.readyState == 'complete') {
        callback();
    }
    else if (registered) {
        window.onload = function() {
            registered();
            callback();
        };
    } else {
        window.onload = function() {
            callback();
        }
    }
}

/*
 *  _____ _                    _
 * |_   _| |__   ___ _ __ ___ (_)_ __   __ _
 *   | | | '_ \ / _ \ '_ ` _ \| | '_ \ / _` |
 *   | | | | | |  __/ | | | | | | | | | (_| |
 *   |_| |_| |_|\___|_| |_| |_|_|_| |_|\__, |
 *                                     |___/
 */

/*
 * unhide theme selection dropdown
 * and give onclick callbacks to links
 */
onReady(function() {
    var buttons = document.getElementsByClassName("theme-selector");
    for (var i=0; i < buttons.length; i++) {
        var a = buttons[i];
        a.onclick = function() {
            set_theme(this.attributes['value'].value);
        };
    }
    document.getElementById('theme-select').style ="display: list-item;";
});

/*
 *  ____       __
 * |  _ \ ___ / _| ___ _ __ ___ _ __   ___ ___  ___
 * | |_) / _ \ |_ / _ \ '__/ _ \ '_ \ / __/ _ \/ __|
 * |  _ <  __/  _|  __/ | |  __/ | | | (_|  __/\__ \
 * |_| \_\___|_|  \___|_|  \___|_| |_|\___\___||___/
 *
 */

onReady(function() {
    var refs = document.getElementsByClassName("footnote-ref");
    for (var i=0; i < refs.length; i++) {
        var r = refs[i];

        // ignore if reference is linked from another reference

        var div = r.parentNode.parentNode.parentNode.parentNode.parentNode;
        // expect: |          |          |          |          |
        //        a.sup       .p         .li        .ol        .div.footnote
        // -or-    |          |          |          |          |
        //        a.sup       .p         .article   .main      .body

        if (div.classList.contains('footnote')) {
            break;
        }

        var doMouseover = function() {
            document.getElementById(
                this.getAttribute('href').replace('#', '')
            ).classList.add('active-ref');
        };
        var doMouseout = function() {
            document.getElementById(
                this.getAttribute('href').replace('#', '')
            ).classList.remove('active-ref');
        };
        var doClick = function() {
            document.getElementById(
                this.getAttribute('href').replace('#', '')
            ).classList.remove('active-ref');
            return true;
        };

        r.onmouseover = doMouseover;
        r.onmouseout = doMouseout;
        r.onclick = doClick;
    }
});

/*   ____                 _ _   _____     _
 *  / ___|  ___ _ __ ___ | | | |_   _| __(_) __ _  __ _  ___ _ __ ___
 *  \___ \ / __| '__/ _ \| | |   | || '__| |/ _` |/ _` |/ _ \ '__/ __|
 *   ___) | (__| | | (_) | | |   | || |  | | (_| | (_| |  __/ |  \__ \
 *  |____/ \___|_|  \___/|_|_|   |_||_|  |_|\__, |\__, |\___|_|  |___/
 *                                          |___/ |___/
 */

function bindScrollTriggers(element, over_cb, out_cb) {
    // register scroll listeners for element's bounding rectangle

    var scroll_listener = function listener() {
        // when element is completely in view, call call over_cb
        // when no longer completely in view, call out_cb

        var window_top = scrollY;
        var window_bottom = scrollY + window.innerHeight;

        if (window_bottom > listener.top &&
            window_top < listener.bottom) {
            if (!listener.active) {
                listener.active = true;
                over_cb();
            }
        } else if (listener.active) {
            listener.active = false;
            out_cb();
        }
    };
    scroll_listener.active = false;

    var resize_listener = function() {
        // update scroll_listener's coordinates

        var rect = element.getBoundingClientRect();

        // store coordinates relative to document
        scroll_listener.top = rect.top + scrollY;
        scroll_listener.bottom = rect.bottom + scrollY;
    };

    window.addEventListener('scroll', scroll_listener);
    window.addEventListener('resize', resize_listener);
    resize_listener();
}

/*       _          _                 _   _
 *      / \   _ __ (_)_ __ ___   __ _| |_(_) ___  _ __  ___
 *     / _ \ | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|
 *    / ___ \| | | | | | | | | | (_| | |_| | (_) | | | \__ \
 *   /_/   \_\_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|___/
 */

/*
 * Collect functions which update components when called.
 * These function will be called with (f, t) arguments,
 * where f is frame number since the function was registered.
 * and t is the unix time in milliseconds.
 *
 * Register such functions with `addAnimation(update_func)`
 *
 * Deregister them with `removeAnimation(update_func)`
 */

var _animations = [];
var _animation_frame_counts = [];
var _animation_loop_running = false;

function addAnimation(update_func) {
    _animations.push(update_func);
    _animation_frame_counts.push(0);

    if (!_animation_loop_running) {
        window.requestAnimationFrame(_doAnimation);
    }
};

function removeAnimation(update_func) {
    var i = _animations.indexOf(update_func);
    if (i == -1) {
        throw 'function not in _animations';
    } else {
        _animations.splice(i, 1);
        _animation_frame_counts.splice(i, 1);
    }
}

function _doAnimation() {
    _animation_loop_running = true;

    var t = (new Date()).getTime();
    for (var i=0; i < _animations.length; i++) {
        var f = _animation_frame_counts[i];
        _animations[i](f, t);
        _animation_frame_counts[i] += 1;
    }

    if (_animations) {
        window.requestAnimationFrame(_doAnimation);
    } else {
        _animation_loop_running = false;
    }
}

onReady(_doAnimation);