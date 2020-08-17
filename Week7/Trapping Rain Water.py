class Solution:
    def trap(self, x: List[int]) -> int:
        l=len(x)
        if not x:return 0
        y=[0 for i in range(l)]
        ans=0
        y[0]=x[0]
        for i in range(1,l-1):
            y[i]=max(y[i-1],x[i])
        ma=x[-1]
        for i in range(l-2,0,-1):
            if y[i]>x[i]:
                if ma>x[i]:
                    ans+= min(ma,y[i])-x[i]
            ma=max(ma,x[i])
        return ans
