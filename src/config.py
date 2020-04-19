import os

config = {
    'debug': os.getenv('DEBUG', 'True').lower() == 'true',
    'sql_db_url': os.getenv('DATABASE_URL', 'postgres://master:local_dev@localhost:5432/lead_collector'),
    'mongo_web_uri': os.getenv('MONGO_WEB_URL', 'mongodb://localhost:27017/lead_zeppelin_dev'),
    'mongo_jobs_uri': os.getenv('MONGO_JOBS_URL', 'mongodb://localhost:27017/lead_zeppelin_dev_jobs'),
    'redis_uri': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    'web_port': int(os.getenv('PORT', '5000'))
}
