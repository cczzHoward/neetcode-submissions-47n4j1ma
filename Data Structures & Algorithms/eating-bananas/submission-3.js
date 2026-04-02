class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let left = 1;
        let right = Math.max(...piles);
        let res = right;

        while (left <= right) {
            console.log(left,right,res);
            let mid = Math.floor((left+right)/2);
            let hours = 0;

            for (let pile of piles) {
                hours += Math.ceil(pile/mid);
            }

            if (hours <= h) {
                res = Math.min(res, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
}
