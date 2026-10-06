# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# helper_notebook

dbutils.widgets.text("name", "default_name")
dbutils.widgets.dropdown("radius", "5", ["5", "10", "20"], "Radius")

# COMMAND ----------

name = dbutils.widgets.get("name")
radius = int(dbutils.widgets.get("radius"))

# COMMAND ----------

def greet_user(name):
    return f"Hello, {name}!"

def area_of_circle(r):
    return 3.14159 * r**2

circle_area = area_of_circle(radius)

# COMMAND ----------

print(f"Helper notebook executed with name={name}, radius={radius}")
print(greet_user(name))
print(circle_area)