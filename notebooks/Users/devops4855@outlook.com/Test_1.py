# Databricks notebook source
list = spark.createDataFrame([('sk',1),('bk',2)],['name','no'])
display(list)