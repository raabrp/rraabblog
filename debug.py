#!/usr/bin/env python3

import logging
import pelican as plcn
import multiprocessing
import cProfile
import pstats
import sys

logger = plcn.logger
parse_arguments = plcn.parse_arguments
init_logging = plcn.init_logging
get_instance = plcn.get_instance
FileSystemWatcher = plcn.FileSystemWatcher
Readers = plcn.Readers
__version__ = plcn.__version__

def autoreload(*args, **kwargs):
    cProfile.runctx('plcn.autoreload(*args, **kwargs)', globals(), locals(), 'autoreload.prof')

def listen(*args, **kwargs):
    cProfile.runctx('plcn.listen(*args, **kwargs)', globals(), locals(), 'listen.prof')

def main():

    args = parse_arguments(None)

    logs_dedup_min_level = getattr(logging, args.logs_dedup_min_level)

    init_logging(
        args.verbosity, args.fatal,
        logs_dedup_min_level=logs_dedup_min_level
    )

    logger.debug('Pelican version: %s', __version__)
    logger.debug('Python version: %s', sys.version.split()[0])

    try:
        pelican, settings = get_instance(args)

        # args.autoreload = True
        # args.listen = True

        if args.autoreload and args.listen:
            excqueue = multiprocessing.Queue()
            p1 = multiprocessing.Process(
                target=autoreload,
                args=(args, excqueue))
            p2 = multiprocessing.Process(
                target=listen,
                args=(settings.get('BIND'), settings.get('PORT'),
                      settings.get("OUTPUT_PATH"), excqueue))
            p1.start()
            p2.start()
            exc = excqueue.get()
            p1.terminate()
            p2.terminate()
            if exc is not None:
                logger.critical(exc)
        elif args.autoreload:
            autoreload(args)
        elif args.listen:
            listen(settings.get('BIND'), settings.get('PORT'),
                   settings.get("OUTPUT_PATH"))
        else:
            watcher = FileSystemWatcher(args.settings, Readers, settings)
            watcher.check()
            pelican.run()
    except KeyboardInterrupt:
        logger.warning('Keyboard interrupt received. Exiting.')
    except Exception as e:
        logger.critical('%s', e)

        if args.verbosity == logging.DEBUG:
            raise
        else:
            sys.exit(getattr(e, 'exitcode', 1))

if __name__ == "__main__":
    main()
    # cProfile.runctx('main()', globals(), locals(), 'main.prof')
