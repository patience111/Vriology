class AnonymousSurvey():
    """collection anonymous answers to a survey quetions."""
    def __init__(self,question):
        """store a question, and prepare to store response."""
        self.question=question
        self.responses=[]
    def show_question(self):
        """show the survey question."""
        print(question)
    def store_response(self,new_response):
        """store a single response to the survey."""
        self.responses.append(new_response)
    def show_results(self):
        """show all the responses that have been given."""
        print('Survey results:')
        for response in responses:
            print('- '+response)
    
