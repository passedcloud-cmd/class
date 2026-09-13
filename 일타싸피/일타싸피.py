import math

start = (1, 1)
end = (2, 2)

a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)

radian = math.atan(b/a)

print(f'degrees: {math.degrees(radian)}')

# 수구(my ball) (wx, wy)에서 목표 지점 (tx, ty)로 공을 보내는 일타싸피 각도
# angle = math.degrees(math.atan2(tx - wx, ty - wy)) % 360


# math.dist(p, q)는 두 점을 그대로 받아 거리를
# math.hypot(dx, dy)는 좌표 차이를 받아 거리를 돌려줍니다.

my_ball = (40, 40)
target_ball = (120, 90)

# 방법 1) 두 점을 그대로 넘기기
print(math.dist(my_ball, target_ball))  # 94.33981132056604

# 방법 2) 좌표 차이를 넘기기
delta_x = target_ball[0] - my_ball[0]
delta_y = target_ball[1] - my_ball[1]
print(math.hypot(delta_x, delta_y))  # 94.33981132056604


# math.atan2(y, x) :  기울기가 아닌 y좌표와 x좌표를 별도의 인자로 받음. 두 값의 부호를 모두 고려하여 사분면 중 어디에 있는지 파악 가능. -180도부터 180도까지 각도 반환. 또한 x가 0이어도(수직 방향이어도) 오류를 내지 않음.

a = math.degrees(math.atan2(-2, 2)) # x = 2, y = -2
print(a) # -45

print('===================\n')

# 기준점A (0,0)
origin_x, origin_y = 0, 0

# 목표 지점들의 좌표 리스트
target_points = [(1, 2), (-2, -3), (3, 1), (-1, 4)]

# 각 목표 지점의 정보를 저장할 리스트
point_info_list = []

# 모든 목표 지점을 순회하며 정보 계산
for point_x, point_y in target_points:
    # 1. 거리 계산하기
    # 거리계산1 : 피타고라스의 정리
    distance_from_origin = math.sqrt((point_x - origin_x) ** 2 + (point_y - origin_y) ** 2)
    # 거리계산2: math.dist()
    distance_from_origin2 = math.dist((origin_x, origin_y), (point_x, point_y))
    # 거리계산3: math.hypot()
    distance_from_origin3 = math.hypot(point_x - origin_x, point_y, origin_y)

    # 2. 각도 계산(atan2 활용)
    angle_radians = math.atan2(point_y - origin_y, point_x - origin_x)
    angle_degrees = math.degrees(angle_radians)

    # 계산된 정보를 리스트에 추가.
    # 데이터 구조를 튜플로.
    point_data = (distance_from_origin, angle_degrees, point_x, point_y)
    point_info_list.append(point_data)

# 4. 거리순으로 정렬. .sort()를 쓰면 오름차순
point_info_list.sort()

# 5. 두 번째로 가까운 점의 정보 선택
second_closest_point = point_info_list[1]

# 6. 결과 출력
distance = second_closest_point[0]
angle = second_closest_point[1]
point_coords = second_closest_point[2]

print(f'점의 위치: {point_coords}, 거리: {distance: .2f} 각도: {angle:.2f}°')
#target_points  리스트에 있는 (1, 2), (-2, -3), (3, 1), (-1, 4) 등 어떤 사분면의 점이든 atan2()는 헷갈리지 않고 고유한 각도를 반환

print('================\n싸피 앵글 = math.degrees(math.atan2(delta_x, delta_y)) % 360\n')
#일타싸피의 각도 방향은 나침반. 12시 방향부터 시계방향으로 돈다.
# atan2의 인자 순서를 바꾸면 됨
# atan2의 반환 범위는 −𝜋∼𝜋이므로 % 360을 함
def to_ssafy_angle(delta_x, delta_y):
    radians = math.atan2(delta_x, delta_y)
    return math.degrees(radians) % 360

directions = [
    ('12시(위)', 0, 10),
    ('1시 30분', 10, 10),
    ('3시(오른쪽)', 10, 0),
    ('4시 30분', 10, -10),
    ('6시(아래)', 0, -10),
    ('7시 30분', -10, -10),
    ('9시(왼쪽)', -10, 0),
    ('10시 30분', -10, 10),
]
for name, delta_x, delta_y in directions:
    angle = to_ssafy_angle(delta_x, delta_y)
    print(f'{name}: {angle}')

print('\n================\n목적구 뒤에 있는 유령 공의 좌표 구하기\n')
#수구 W(40, 40)  /  목적구 T(120, 90)  /  홀 H(240, 160)  /  공 지름 D = 10

# [1] 목적구 -> 홀 방향 벡터를 구한다
    #(240 - 120, 160 - 90) = (120, 70)
    #길이 = 138.92

# [2] 길이를 1로 만든다 (단위 벡터)
    #(120 / 138.92, 70 / 138.92) = (0.86, 0.50)

# [3] 접점 = 목적구에서 '홀 반대 방향'으로 공 지름만큼 물러난 자리
    #(120, 90) - (0.86, 0.50) * 10 = (111.36, 84.96)
    #더하기가 아니라 빼기! (홀에서 멀어지는 쪽)

# [4] 수구 -> 접점 좌표 차이
    # dx = 111.36 - 40 = 71.36
    # dy =  84.96 - 40 = 44.96

# [5] 일타싸피 각도로 변환
result = math.degrees(math.atan2(71.36, 44.96)) % 360
print(f'{result:.2f}도') # 57.79

#연습 코드
ball_diameter = 10
def to_ssafy_angle(delta_x, delta_y):
    """좌표 차이를 알면 일타싸피 각도로 변환"""
    return math.degrees(math.atan2(delta_x, delta_y) % 360)

def aim_at(white_ball, target_ball, hole):
    """수구로 목적구를 쳐서 hole에 넣기 위한 (각도, 세기, 접점)을 반환"""
    # 1. 목적구 -> 홀 방향 벡터
    to_hole_x = hole[0] - target_ball[0]
    to_hole_y = hole[1] - target_ball[1]
    hole_distance = math.hypot(to_hole_x, to_hole_y)

    # 2. 길이를 1로 정규화
    unit_x = to_hole_x / hole_distance
    unit_y = to_hole_y / hole_distance

    # 3. 접점 좌표 = 목적구에서 홀 반대 방향으로 공 지름만큼 물러난 자리
    contact_x = target_ball[0] - unit_x * ball_diameter
    contact_y = target_ball[1] - unit_y * ball_diameter

    # 4. 수구 -> 접점 방향을 일타싸피 각도로 변환
    delta_x = contact_x - white_ball[0]
    delta_y = contact_y - white_ball[1]
    angle = to_ssafy_angle(delta_x, delta_y)

    # 5. 세기는 수구 -> 접점 거리를 기준으로 잡고 상황에 맞게 보정
    power = math.hypot(delta_x, delta_y)

    return angle, power, (contact_x, contact_y)

angle, power, contact = aim_at((40, 40), (120, 90), (240, 160))
print(f'접점: {contact[0]:.2f}, {contact[1]:.2f}')
print(f'각도: {angle:.2f}도, 세기: {power:.2f}')

# 세기는 수구->접점 거리와 목적구->홀 거리를 모두 더한 값을 기준으로 잡음. 여기에 배수(계수)를 곱해 보정.
# 세기 = (거리1 + 거리2) *1.2
# 계수는 실험으로 찾는 것.

print('\n================\n연습 1. 목적구를 직접 조준하는 각도 구하기\n')

def aim_direct(white_ball, target_ball):
    """수구에서 목적구 중심을 향하는 일타싸피 각도를 반환한다."""
    # TODO: 목표에서 수구를 빼서 좌표 차이를 구하세요
    # [힌트] 순서는 항상 '목표 - 수구' 입니다
    delta_x = target_ball[0] - white_ball[0]
    delta_y = target_ball[1] - white_ball[1]

    # TODO: atan2로 라디안을 구하세요
    # [힌트] 일타싸피는 +y축이 0도이므로 인자 순서를 뒤집습니다
    radians = math.atan2(delta_x, delta_y)

    # TODO: 도로 변환하고 0 ~ 360 범위로 정규화하세요
    # [힌트] math.degrees() 와 % 360
    angle = math.degrees(radians) % 360

    return angle


# 검증: 아래 네 줄이 각각 0.0, 90.0, 180.0, 270.0 이 나와야 합니다
print(aim_direct((50, 50), (50, 90)))
print(aim_direct((50, 50), (90, 50)))
print(aim_direct((50, 50), (50, 10)))
print(aim_direct((50, 50), (10, 50)))

print('\n================\n연습 2. 가장 가까운 지점 고르기\n')
def nearest_point(origin, points):
    """origin에서 가장 가까운 점의 좌표를 반환한다."""
    # TODO: min()의 key 인자에 '기준점까지의 거리'를 계산하는 람다를 넘기세요
    # [힌트] math.dist(origin, point)
    
    return min(points, key=lambda points: math.dist(origin, points))
    # min(리스트, key=...) -> "이 리스트에서 최솟값을 찾을 건데, 각 항목을 비교할 때 key로 지정한 함수의 결과값을 기준으로 비교해라"
    # lambda(함수를 만든다) points:(매개변수) math.dist(origin, point)(이 함수 값을 리턴할 것)

candidates = [(12, 80), (95, 25), (140, 60), (30, 15)]

print(nearest_point((60, 50), candidates))   # (95, 25)
print(nearest_point((130, 70), candidates))  # (140, 60)

print('\n================\n연습 3. 접점을 거쳐 조준하기 (종합)\n')
BALL_DIAMETER = 10


def aim_at(white_ball, target_ball, hole):
    """수구로 목적구를 쳐서 hole에 넣기 위한 (각도, 세기)를 반환한다."""
    # TODO: 목적구 -> 홀 방향 벡터와 그 길이를 구하세요
    to_hole_x = hole[0] - target_ball[0]
    to_hole_y = hole[1] - target_ball[1]
    hole_distance = math.hypot(to_hole_x, to_hole_y)

    # TODO: 길이를 1로 만드는 단위 벡터를 구하세요
    # [힌트] 각 성분을 길이로 나눕니다
    unit_x = to_hole_x / hole_distance
    unit_y = to_hole_y / hole_distance

    # TODO: 접점 좌표를 구하세요
    # [힌트] 목적구에서 '홀 반대 방향'이므로 더하기가 아니라 빼기입니다
    contact_x = target_ball[0] - unit_x * BALL_DIAMETER
    contact_y = target_ball[1] - unit_y * BALL_DIAMETER

    # TODO: 수구 -> 접점 방향의 일타싸피 각도와 거리를 구하세요
    delta_x = contact_x - white_ball[0]
    delta_y = contact_y - white_ball[1]
    angle = math.degrees(math.atan2(delta_x, delta_y)) % 360
    power = math.dist(white_ball, (contact_x, contact_y))
    # power = math.hypot(delta_x, delta_y)
    return angle, power


print(aim_at((40, 40), (120, 90), (240, 160)))
# 기대 결과: 각도 57.79도 부근, 세기 84.35 부근