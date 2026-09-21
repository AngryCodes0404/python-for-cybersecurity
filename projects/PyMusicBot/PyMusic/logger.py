class PyMusicLogger:
    @staticmethod
    def success(msg):
        msg = "✅ " + msg
        print(msg)
    
    @staticmethod
    def info(msg):
        msg = "ℹ️ " + msg
        print(msg)
    
    @staticmethod
    def warning(msg):
        msg = "⚠️  " + msg
        print(msg)
    
    @staticmethod
    def error(msg):
        msg = "🛑 " + msg
        print(msg)
    
    @staticmethod
    def playing(msg):
        msg = "🎵 " + msg
        print(msg)
    
    @staticmethod
    def playlist(msg):
        msg = "🎶 " + msg
        print(msg)
    
    
    @staticmethod
    def printSpace():
        print("===================================================")
