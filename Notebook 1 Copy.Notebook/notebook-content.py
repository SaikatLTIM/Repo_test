# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "146052ad-ed7e-4688-b952-ff5aa7717428",
# META       "default_lakehouse_name": "Saikat_Learning_LH",
# META       "default_lakehouse_workspace_id": "682ed0ff-8385-4ba2-ae1d-1cc231862788",
# META       "known_lakehouses": [
# META         {
# META           "id": "146052ad-ed7e-4688-b952-ff5aa7717428"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
print('Saikat')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM Saikat_Learning_LH.table_employee LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
