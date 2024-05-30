from website import create_app

app = create_app()

if __name__ == '__main__':  # when run this file only then run server
    app.run(debug=True)  # run flask application, any change, re-run server
