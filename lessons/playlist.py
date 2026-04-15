class Playlist:
    # магические методы, dunder - double underscore
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"<Playlist object, name: {self.name}>"

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        print("items in contains", item)
        return item in self.songs

    def __bool__(self):
        return len(self.songs) > 0


if __name__ == "__main__":
    pop = Playlist("pop playlist", songs=["Shape of my heart", "Bad guy"])
    print(pop)
    print(len(pop))
    print("Billy Jiens" in pop)
    print("Shape of my heart" in pop)
    if pop:
        print("Playlist is not empty")
    else:
        print("Playlist is empty")
