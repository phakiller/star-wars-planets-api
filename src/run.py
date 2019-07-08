from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=6606,
        debug=app.config.APPLICATION_DEBUG,
        workers=app.config.APPLICATION_WORKERS_NUMBER,
    )
