"""
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Time Complexity = O(N)
Space Complexity = O(1)
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if not coordinates:
            return False      
        
        if len(coordinates) == 2:
            return True
        
        p_x = p_y = None
        #Decions points
        x_1, y_1 = coordinates[0]
        x_2, y_2 = coordinates[1]
        incline = straight = vertical = angle = None
        
        
        if abs(x_1 - x_2) > 0 and y_1 == y_2:
            straight = True
            
        elif abs(y_1 - y_2) > 0 and x_1 == x_2:
            vertical = True

        else:
            incline = True
            angle = (y_2 - y_1)/(x_2 - x_1)


        for point in coordinates[1:]:
            if len(point) != 2:
                return False
            
            x, y = point
            if not p_x and not p_y:
                p_x, p_y = x, y
                continue
            
            if incline:
                if x - p_x == 0:
                    return False
                if angle == (y - p_y)/(x - p_x):
                    p_x, p_y = x, y
                    continue
                else:
                    return False
                
            if straight:
                if abs(x - p_x) > 0 and y == p_y:
                    p_x, p_y = x, y
                    continue
                else:
                    return False
            
            if vertical:
                if abs(y - p_y) > 0 and x == p_x:
                    p_x, p_y = x, y
                    continue
                else:
                    return False
            
        return True


# Simple solution using only angle
# Angle should be same b/w two points

class Solution:
    def checkStraightLine(self, coordinates):
        
        if not coordinates:
            return False      
        
        if len(coordinates) == 2:
            return True
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        angle = None
        if x2 - x1 == 0:
            angle = 'infinity'

        else:
            angle = (y2- y1)/(x2 - x1)

        for point in coordinates[2:]:
            x, y = point
            
            if angle == 'infinity':
                if x - x2 == 0:
                    continue 
                else:
                    return False

            elif angle == (y - y2) / (x - x2):
                continue

            else:
                return False

        return True

        
obj = Solution()
print(obj.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
        
