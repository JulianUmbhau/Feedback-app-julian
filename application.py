from application import application
from application import ngrok

# if __name__ == '__main__':
#     application.run()
if __name__ == '__main__':
    application.run(host='0.0.0.0', debug = True)

    # application.run(debug = True)