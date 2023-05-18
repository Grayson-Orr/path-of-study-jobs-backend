BOT_NAME = "job"
SPIDER_MODULES = ["job.spiders"]
NEWSPIDER_MODULE = "job.spiders"
ROBOTSTXT_OBEY = False
LOG_LEVEL = "WARNING"
DOWNLOAD_DELAY = 2
ITEM_PIPELINES = {
    'job.pipelines.JobPipeline': 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
