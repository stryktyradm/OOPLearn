class TrackLine:
    
    def __init__(self, x, y, sp=0):
        self.to_x = x
        self.to_y = y
        self.speed = sp


class Track:

    def __init__(self, start_x=0, start_y=0):
        self.segments = [TrackLine(start_x, start_y)]

    def add_track(self, tr):
        if not isinstance(tr, TrackLine):
            raise TypeError('Сегмент маршрута должен быть объектом TrackLine')
        self.segments.append(tr)

    def get_tracks(self):
        return tuple(self.segments)
    
    @classmethod
    def __validate_data(cls, other):
        if not isinstance(other, cls):
            raise TypeError('Несравниваемый объект')
        return len(other)

    def __eq__(self, other):
        l = self.__validate_data(other)
        return len(self) == l

    def __lt__(self, other):
        l = self.__validate_data(other)
        return len(self) < l
    
    def __len__(self):
        length = 0
        lines = self.get_tracks()
        for i in range(len(lines)-1):
            length += ((lines[i+1].to_x - lines[i].to_x)**2 + (lines[i+1].to_y - lines[i].to_y)**2)**0.5  
        return int(length)

