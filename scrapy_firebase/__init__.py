# -*- coding: utf-8 -*-

from scrapy.exporters import BaseItemExporter

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class FirebasePipeline(BaseItemExporter):
    def load_spider(self, spider):
        self.crawler = spider.crawler
        self.settings = spider.settings
        self.keys = self.settings["FIREBASE_KEYS"]

    def open_spider(self, spider):
        self.load_spider(spider)

        configuration = {
            "credential": credentials.Certificate(
                self.settings["FIREBASE_CERTIFICATE"]
            ),
            "options": {"databaseURL": self.settings["FIREBASE_DATABASE"]},
        }

        firebase_admin.initialize_app(**configuration)
        self.ref = db.reference(self.settings["FIREBASE_REF"])

    def process_item(self, item, spider):
        item = dict(self._get_serialized_fields(item))

        child = self.ref.child("/".join([item[key] for key in self.keys]))
        child.set(item)
        return item

    def close_spider(self, spider):
        pass
