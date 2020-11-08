import unittest


class CallCenter(object):
    def __init__(self, respondents, managers, director):
        self.respondents = respondents
        self.managers = managers
        self.director = director
        self.respondent_queue = []
        self.call_queue = []
        for respondent in respondents:
            respondent.call_center = self
            if not respondent.call:
                self.respondent_queue.append(respondent)

    def route_call(self, call):
        # if there is any respondent => take call
        # else append to call queue
        if len(self.respondent_queue):
            self.respondent_queue.pop(0).take_call(call)
        else:
            self.call_queue.append(call)

    def route_respondent(self, respondent):
        if len(self.call_queue):
            respondent.take_call(self.call_queue.pop(0))
        else:
            self.respondent_queue.append(respondent)


class Call:
    def __init__(self, issue):
        self.issue = issue
        self.employee = None

    def resolve(self, handled):
        if handled:
            self.issue = None
        self.employee.finish_call(handled)

    def apologize_and_hangup(self):
        self.employee = None
        print('our line is too busy! Please take another call')


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.call = None

    def take_call(self, call):
        # if the employee is busy, reassign the call to their manager
        if self.call:
            self.escalate(call)
        else:
            self.call = call
            self.call.employee = self

    def escalate(self, call):
        if self.manager:
            self.manager.take_call(call)
        else:
            call.apologize_and_hangup()

        # free the call
        self.call = None

    def finish_call(self, handled=True):
        if not handled:
            # try to assign the call to manager
            if self.manager:
                self.manager.take_call(self.call)
            else:
                self.call.apologize_and_hangup()
        self.call = None


class Respondent(Employee):
    def finish_call(self, handled=True):
        # search for finish_call method from parent of Respondent (that is Employee)
        super(Respondent, self).finish_call(handled)

        # check any available call for the respondent after finish this call
        self.call_center.route_respondent(self)


class Manager(Employee):
    pass


class Director(Employee):
    def __init__(self, name):
        # re initiate with manager = None
        super(Director, self).__init__(name, None)


class Test(unittest.TestCase):
    def test_call_center(self):
        hieu = Director('Hieu')
        anh = Manager("Anh", hieu)
        yen = Manager("Yen", hieu)
        toan = Respondent('Toan', yen)
        linh = Respondent('Linh', yen)
        manh = Respondent('Manh', anh)
        van = Respondent('Van', anh)

        center = CallCenter([toan, linh, manh, van], [anh, yen], hieu)

        call1 = Call("The toilet")
        call2 = Call("The webpage")
        call3 = Call("The email")
        call4 = Call("The lizard")
        call5 = Call("The cloudy weather")
        call6 = Call("The noise")

        self.assertEqual(len(center.respondent_queue), 4)
        center.route_call(call1)
        center.route_call(call2)
        self.assertEqual(len(center.respondent_queue), 2)
        center.route_call(call3)
        center.route_call(call4)
        self.assertEqual(len(center.respondent_queue), 0)
        center.route_call(call5)
        center.route_call(call6)
        self.assertEqual(center.call_queue, [call5, call6])
        call1.resolve(True)
        self.assertEqual(call1.issue, None)
        self.assertEqual(center.call_queue, [call6])
        call3.resolve(False)
        self.assertEqual(anh.call, call3)
        call3.resolve(False)
        self.assertEqual(hieu.call, call3)
        self.assertEqual(anh.call, None)


if __name__ == '__main__':
    unittest.main()
