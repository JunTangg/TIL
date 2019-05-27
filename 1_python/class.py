class Course:
    name = '4차4기'

    def introduce(self):
        return self.name


course = Course()
course.introduce()


def greeting():
    return 'Hello!'

greeting().