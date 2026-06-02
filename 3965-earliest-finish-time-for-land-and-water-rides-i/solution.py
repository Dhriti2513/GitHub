class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        min_finish = float('inf')
        
        # Scenario 1: Land ride first, then Water ride
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                water_start = max(land_finish, waterStartTime[j])
                water_finish = water_start + waterDuration[j]
                if water_finish < min_finish:
                    min_finish = water_finish
                    
        # Scenario 2: Water ride first, then Land ride
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]
            for i in range(len(landStartTime)):
                land_start = max(water_finish, landStartTime[i])
                land_finish = land_start + landDuration[i]
                if land_finish < min_finish:
                    min_finish = land_finish
                    
        return min_finish
        
