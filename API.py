import http.client
from codecs import encode

def create_game(team1, team2, board_size = 12, target = 6):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=type;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("game"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=teamId1;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(team1)))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=teamId2;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(team2)))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=gameType;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("TTT"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=boardSize;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(board_size)))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=target;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(target)))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
      'x-api-key': 'b89df8b5c86bc18bb889',
      'userid': '1063',
      'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    if "FAIL" in response:
        print(response)
        
    # return game id
    x = response.index('"gameId')
    return response[x:x+13]

def make_move(game, team, row, col):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=type;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("move"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=gameId;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(game)))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=teamId;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode(str(team)))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=move;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    move = str(row) + ',' + str(col)
    dataList.append(encode(move))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
      'x-api-key': 'b89df8b5c86bc18bb889',
      'userid': '1063',
      'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    if "FAIL" in response:
        print('make move', row, col)
        print(response)

def get_board_string(game):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
      'x-api-key': 'b89df8b5c86bc18bb889',
      'userid': '1063'
    }
    string = "/aip2pgaming/api/index.php?type=boardString&gameId=" + str(game)
    conn.request("GET", string, payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    response = data.decode("utf-8")
    if "FAIL" in response:
        print('get board string')
        print(response)
        return
    
    # print board
    output = response.split('","')[0].split('":"')[1]
    output = output.split('\\n')
    for line in output:
        print(line)

def get_board_map(game):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
      'x-api-key': 'b89df8b5c86bc18bb889',
      'userid': '1063'
    }
    string = "/aip2pgaming/api/index.php?type=boardMap&gameId=" + str(game)
    conn.request("GET", string, payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    response = data.decode("utf-8")
    if "FAIL" in response:
        print('get board map')
        print(response)
        return
    if 'null' in response:
        return {}
    
    # turn response into dictionary of all moves
    output = response.split(',"')[0].split('":"')[1].replace('{', '').replace('}', '').split('\\",\\"')
    moves = {}
    for move in output:
        move = move.replace('\\"', '').split(':')
        if len(move) > 0:
            moves.update({move[0] : move[1]})
    
    return moves

def get_moves(game):
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
      'x-api-key': 'b89df8b5c86bc18bb889',
      'userid': '1063'
    }
    string = "/aip2pgaming/api/index.php?type=moves&gameId=" + str(game) + "&count=1"
    conn.request("GET", string, payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    # return most recent move
    response = data.decode("utf-8")
    moveX_start = response.index('"moveX":')
    moveY_start = response.index(',"moveY":')
    moveY_end = response.index('}],"code')
    row = response[moveX_start+9:moveY_start-1]
    col = response[moveY_start+10:moveY_end-1]
    return (int(row), int(col))

get_moves(3196)