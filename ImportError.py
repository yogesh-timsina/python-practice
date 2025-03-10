try:
    import non_existent_module
except ImportError as e:
    print("There is error",e)