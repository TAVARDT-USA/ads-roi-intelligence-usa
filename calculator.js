/**
 * TAVARDT Elite Paid Media ROI Intelligence
 * Description: Mathematical modeling for paid traffic scale and diminishing returns projection.
 */

'use strict';

const ROI_Calculator = {
    /**
     * Calculate core performance metrics
     * @param {number} spend
     * @param {number} revenue
     */
    calculateBaseMetrics: function(spend, revenue) {
        if (spend <= 0) return { roas: 0, roi: 0 };
        const roas = (revenue / spend).toFixed(2);
        const roi = (((revenue - spend) / spend) * 100).toFixed(2);
        return {
            roas: parseFloat(roas),
            roi: parseFloat(roi)
        };
    },

    /**
     * Scale projection using TAVARDT diminishing returns coefficient
     * @param {number} currentSpend
     * @param {number} targetSpend
     * @param {number} currentROAS
     * @param {number} decayFactor
     */
    projectScale: function(currentSpend, targetSpend, currentROAS, decayFactor = 0.85) {
        if (currentSpend <= 0 || targetSpend <= 0 || currentROAS <= 0) {
            return { projectedROAS: 0, projectedRevenue: 0, efficiencyLoss: 0 };
        }
        const spendRatio = targetSpend / currentSpend;
        const projectedROAS = (currentROAS * Math.pow(spendRatio, decayFactor - 1)).toFixed(2);
        const projectedRevenue = (targetSpend * projectedROAS).toFixed(2);
        const efficiencyLoss = ((1 - (projectedROAS / currentROAS)) * 100).toFixed(2);

        return {
            projectedROAS: parseFloat(projectedROAS),
            projectedRevenue: parseFloat(projectedRevenue),
            efficiencyLoss: parseFloat(efficiencyLoss)
        };
    }
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = ROI_Calculator;
}
