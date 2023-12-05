from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)


mongo_uri = "mongodb+srv://FestivalAPI:12Capital!@cluster0.w4kfv28.mongodb.net/"
client = MongoClient(mongo_uri)