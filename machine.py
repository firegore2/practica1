class Machine(object):
    """clase que forma parte del motor del juego"""
    cars = []
    save = []


    def start(self,levelfile):
        print("este es el fichero de guardado "+levelfile)


machine=Machine()
machine.start("save.txt")