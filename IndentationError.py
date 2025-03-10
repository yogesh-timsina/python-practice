try:
    exec("""
    def example():
    print("Hello")
     """)
except IndentationError as e:
    print("Error:",e)
    