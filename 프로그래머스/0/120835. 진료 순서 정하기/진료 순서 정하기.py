def solution(emergency):
    emergencyArr = sorted(emergency, reverse=True)
    return [emergencyArr.index(v)+1 for v in emergency]