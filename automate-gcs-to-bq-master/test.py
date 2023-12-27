"parameters": {
        "javascriptTextTransformGcsPath": "gs://big-gcs/udf.js",
        "JSONPath": "gs://big-gcs/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "leafy-summer-405104:user_data.users",
        "inputFilePattern": "gs://bkt-landing-zo/user.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://big-gcs"
    }