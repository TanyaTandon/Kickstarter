[loggers]
keys=root

[handlers]
keys=fileHandler

[formatters]
keys=formatter

[logger_root]
level=INFO
handlers=fileHandler

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=formatter
args=('logs/logfile.log',)

[formatter_formatter]
format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s