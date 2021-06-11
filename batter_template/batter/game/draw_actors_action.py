from game.action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service
        

    def execute(self, cast):
        actors = cast["paddle"]
        actor = cast["brick"]
        ball = cast["ball"]
        self._output_service.draw_actors(actors)
        self._output_service.draw_actors(actor)
        self._output_service.draw_actors(ball)
        self._output_service.flush_buffer()    
        self._output_service.clear_screen()
