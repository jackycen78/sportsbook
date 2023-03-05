class AllPlayerProps:

    def __init__(self):
        self.games = {}

    def add_prop(self, props):
        for prop in props:

            if prop.player not in self.games:
                self.games[prop.player] = []

            self.games[prop.player].append(prop)