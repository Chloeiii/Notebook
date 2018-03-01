import bottle
import os
import random
#---------------------------------------------------------------------------
game_id = ''
board_width = 0
board_height = 0
#---------------------------------------------------------------------------

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/head2.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'cc',
        "head_type": "tongue",
        "tail_type": "pixel"
    }
                            

#--------------------------------------------------------------------------------------
@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data

    #crate a 2d array for board
    Board = [[0 for x in range(board_width)] for y in range(board_height)] 
    
    #get food location
    my_food_list = []
    food_list = data.get('food')['data']
    for each_food in food_list:
        food_x = each_food['x']
        food_y = each_food['y']
        my_food_list.append([food_x, food_y]) #my_food_list e.g. [[12,1], [23,12], [0,9]]

    #get the location of myself
    my_body_list = []
    body_list = data.get('you')['body']['data']
    for each_segment in body_list:
        segment_x = each_segment['x']
        segment_y = each_segment['y']
        my_body_list.append([segment_x,segment_y]) #my_body_list e.g. [[1,1], [2,1], [2,2]]

    #get the location of other snakes
    enemy_body_list = []
    enemy_list = data.get('snakes')['data']
    for each_enemy in enemy_list:
        each_enemy_snake = []
        for each_enemy_segement in each_enemy['body']['data']:
            enemy_body_x = each_enemy_segement['x']
            enemy_body_y = each_enemy_segement['y']
            each_enemy_snake.append([enemy_body_x, enemy_body_y]) #each_enemy_snake e.g. [[2,3],[2,4]]
        enemy_body_list.append(each_enemy_snake) #enemy_body_list e.g [ [[2,3],[2,4]], [[5,6],[5,7],[5,8]] ]  two snakes
        


    #avoid the tail, calculate the path for nearest food

    #if there's no food (rare condition)
    if len(my_food_list) == 0:
        return{
            'move': 'up'
            'taunt': 'NO FOOD NO GAME!'
        }
    else:
        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)
        print direction
        return {
            'move': direction,
            'taunt': 'I\'m drunk'
        }

#considering tails to be walls, we can use backtrack method
def find_nearest_food(food_list, body_list, enemy_body_list):




#---------------------------------------------------------------------------------------

@bottle.post('/end')
def end():
    data = bottle.request.json
    return {'taunt': 'uh'}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)