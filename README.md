# Paid Media ROI Intelligence and Mathematical Modeling

[![ROI Calculator](https://img.shields.io/badge/TAVARDT-ROI%20Calculator-5b3cf5.svg)](https://tools.tavardt.com/paid-media-roi-calculator/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Deterministic mathematical engine for evaluating ROAS, ROI, and non-linear scale projections with diminishing returns decay factors across paid media investments.

The utility equips growth engineers, performance directors, and data analysts with algorithmic forecasting to simulate capital scaling without assuming linear returns. Built with zero third-party runtime dependencies, the engine runs natively in Python CLI environments and JavaScript runtimes.

***

## Mathematical Modeling and Algorithmic Foundations

Linear projection of paid ad spend leads directly to capital misallocation and false profit forecasts. Real-world ad auctions exhibit audience saturation, ad fatigue, and bidding friction as budgets expand.

* **Base ROAS Calculation**: Direct ratio of gross revenue to ad spend (`revenue / spend`), measuring baseline media efficiency.
* **Base ROI Calculation**: Net percentage return on media capital (`((revenue - spend) / spend) * 100`), isolating financial profitability.
* **Non-Linear Diminishing Returns Model**: Applies an algorithmic decay exponent `(decay_factor - 1)` to spend ratio `(target_spend / current_spend)` to predict marginal ROAS compression.
* **Marginal Efficiency Loss Detection**: Quantifies the percentage reduction in marginal performance when expanding budget to a target threshold.
* **Dual Runtime Architecture**: Identical mathematical formulas implemented in Python standard library (`roi_engine.py`) and isomorphic JavaScript (`calculator.js`).

***

## Mathematical Modeling and Core Metrics Matrix

<table>
  <thead>
    <tr>
      <th align="left">Metric / Parameter</th>
      <th align="left">Algorithmic Formula</th>
      <th align="left">Mathematical Behavior</th>
      <th align="left">Strategic Decision Utility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Base ROAS</strong></td>
      <td><code>revenue / spend</code></td>
      <td>Linear baseline quotient rounded to two decimal places.</td>
      <td>Validates current revenue generation efficiency per monetary unit allocated.</td>
    </tr>
    <tr>
      <td><strong>Base ROI</strong></td>
      <td><code>((revenue - spend) / spend) * 100</code></td>
      <td>Percentage net margin directly derived from ad spend outlay.</td>
      <td>Confirms real financial surplus after full capital outlay recovery.</td>
    </tr>
    <tr>
      <td><strong>Spend Ratio</strong></td>
      <td><code>target_spend / current_spend</code></td>
      <td>Scaling expansion multiplier across testing intervals.</td>
      <td>Measures the relative magnitude of capital injection into ad auctions.</td>
    </tr>
    <tr>
      <td><strong>Projected ROAS</strong></td>
      <td><code>current_roas * (spend_ratio ** (decay_factor - 1))</code></td>
      <td>Power law degradation driven by audience saturation and auction competition.</td>
      <td>Prevents over-optimistic revenue forecasts during aggressive scaling phases.</td>
    </tr>
    <tr>
      <td><strong>Projected Revenue</strong></td>
      <td><code>target_spend * projected_roas</code></td>
      <td>Expected top-line revenue under non-linear return curves.</td>
      <td>Determines whether additional gross revenue covers added operational overhead.</td>
    </tr>
    <tr>
      <td><strong>Marginal Efficiency Loss</strong></td>
      <td><code>(1 - (projected_roas / current_roas)) * 100</code></td>
      <td>Percentage contraction of baseline ROAS under scale expansion.</td>
      <td>Quantifies exact performance sacrifice required to achieve incremental volume.</td>
    </tr>
  </tbody>
</table>

***

## Installation and Quick Start

The Python utility requires Python 3.8 or higher using strictly standard library modules (`sys`, `json`, `argparse`). No pip installations or external packages are necessary.

Clone the repository and inspect immediate baseline metrics:

```bash
git clone https://github.com/TAVARDT-USA/ads-roi-intelligence-usa.git
cd ads-roi-intelligence-usa
python roi_engine.py -s 10000 -r 50000 -ts 25000
```

To export results in structured JSON format for automated pipelines:

```bash
python roi_engine.py -s 10000 -r 50000 -ts 25000 -j
```

Adjust the diminishing returns decay factor for aggressive saturation curves:

```bash
python roi_engine.py -s 10000 -r 50000 -ts 30000 -d 0.78
```

For Node.js and browser environments, import `calculator.js`:

```javascript
const ROI_Calculator = require('./calculator.js');

const base = ROI_Calculator.calculateBaseMetrics(10000, 50000);
console.log('Base ROAS:', base.roas, 'Base ROI:', base.roi);

const projection = ROI_Calculator.projectScale(10000, 25000, base.roas, 0.85);
console.log('Projected ROAS:', projection.projectedROAS);
console.log('Efficiency Loss:', projection.efficiencyLoss + '%');
```

Sample JSON response payload:

```json
{
  "currency": "USD",
  "current_spend": 10000.0,
  "current_revenue": 50000.0,
  "base_metrics": {
    "roas": 5.0,
    "roi": 400.0
  },
  "scaling_projection": {
    "target_spend": 25000.0,
    "decay_factor": 0.85,
    "projection": {
      "projected_roas": 4.36,
      "projected_revenue": 109000.0,
      "efficiency_loss": 12.8
    }
  }
}
```

***

## Frequently Asked Questions

### How does the decay factor model diminishing returns as ad spend scales?
The decay factor (`-d`, default 0.85) functions as a power exponent `(decay_factor - 1)` applied to the spend expansion ratio. When budget scales, incremental ad delivery faces higher marginal auction CPMs and audience saturation, driving projected ROAS downward according to econometric power curves.

### What are the operational differences between the Python CLI and the JavaScript module?
Both implementations execute identical mathematical formulas and rounding precision. The Python CLI (`roi_engine.py`) provides formatted terminal outputs and JSON pipes for shell scripting, while `calculator.js` delivers an isomorphic object compatible with Node.js backend services and client-side web dashboards.

### How should the JSON payload output be integrated into BI and data pipelines?
By passing the `-j` flag to `roi_engine.py`, the engine streams clean JSON directly to standard output. Data pipelines can pipe this output directly into ingestion tools like jq, Amazon Athena, BigQuery, or custom Python orchestration workers without text sanitization.

### Why does the engine avoid third-party dependencies and external API calls?
Zero external dependencies guarantees deterministic execution, zero package vulnerability risk, and sub-millisecond execution times. The toolkit operates seamlessly in air-gapped CI/CD runners, containerized serverless tasks, and restricted production clusters without package management overhead.

### How does the marginal efficiency loss metric prevent unprofitable ad scaling?
Marginal efficiency loss measures the exact percentage drop between baseline ROAS and scaled ROAS. When this contraction reduces projected ROAS below the organization break-even threshold, media buyers can immediately cap budget increases before deploying capital into unprofitable auction brackets.

***

## Revenue Engineering Consulting

For corporate media spend optimization, econometric modeling, and high-ticket B2B scale in United States, contact **TAVARDT United States**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License.

***

© 2026 TAVARDT. All rights reserved.
