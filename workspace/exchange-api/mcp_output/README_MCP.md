# exchange-api (MCP (Model Context Protocol) Service)

## Project Introduction  
`exchange-api` is a lightweight, high‑performance REST service that exposes real‑time currency exchange data. It aggregates data from multiple public sources, merges and normalises it into a single JSON payload, and serves it through a set of well‑defined endpoints. The service is ideal for fintech applications, financial dashboards, or any project that requires up‑to‑date currency rates, conversion utilities, or currency metadata.

Key features:
- **Fast lookup** of exchange rates and currency metadata.
- **Currency conversion** with optional rounding and precision control.
- **Bulk data** endpoints for retrieving all supported currencies or symbols.
- **Extensible** – new data sources can be added by updating the JSON merge scripts.

## Installation Method  
The project is a Node.js application.  
```bash
# Clone the repository
git clone https://github.com/fawazahmed0/exchange-api.git
cd exchange-api

# Install dependencies
npm install

# (Optional) Build the project if you plan to modify the source
npm run build

# Start the service
npm start
```
**Prerequisites**  
- Node.js ≥ 18.x (LTS)  
- npm ≥ 9.x  

The service reads configuration from environment variables. Create a `.env` file in the project root or export the variables directly:

```
PORT=3000          # Port the server will listen on
RATE_LIMIT=1000    # Optional: maximum requests per minute
```

## Quick Start  
Once the server is running, you can interact with it using `curl`, `fetch`, or any HTTP client.

```bash
# Get the latest exchange rates (base USD)
curl http://localhost:3000/rates?base=USD

# Convert 100 EUR to USD
curl http://localhost:3000/convert?from=EUR&to=USD&amount=100

# List all supported currencies
curl http://localhost:3000/currencies
```

**Node example**  
```js
const fetch = require('node-fetch');

(async () => {
  const res = await fetch('http://localhost:3000/convert?from=GBP&to=JPY&amount=50');
  const data = await res.json();
  console.log(data); // { from: 'GBP', to: 'JPY', amount: 50, rate: 155.23, result: 7761.5 }
})();
```

## Available Tools and Endpoints List  

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/rates` | GET | Returns current exchange rates for a specified base currency. Query params: `base` (ISO 4217 code), `symbols` (comma‑separated list). |
| `/convert` | GET | Converts an amount from one currency to another. Query params: `from`, `to`, `amount`. |
| `/currencies` | GET | Lists all supported currencies with metadata (name, symbol, country). |
| `/symbols` | GET | Returns a simple list of currency symbols. |
| `/countries` | GET | Maps currencies to their respective countries. |
| `/health` | GET | Health‑check endpoint; returns status `ok`. |

All responses are JSON. Errors are returned with a `400` or `500` status and a descriptive message.

## Common Issues and Notes  

| Issue | Cause | Fix |
|-------|-------|-----|
| **Node version mismatch** | Using Node < 18 may break ES module syntax. | Upgrade to Node 18+ or adjust the `package.json` to use CommonJS. |
| **Missing `node_modules`** | `npm install` was skipped. | Run `npm install` again. |
| **Port already in use** | Another process is listening on the chosen port. | Change `PORT` in `.env` or stop the conflicting process. |
| **Rate limiting** | Exceeding the `RATE_LIMIT` threshold. | Increase the limit or implement client‑side throttling. |
| **Data not updating** | JSON merge scripts (`other/*.js`) were not re‑run. | Re‑execute the merge scripts or run `npm run update-data`. |
| **Large payloads** | `/currencies` returns ~25 k entries. | Use pagination (`?page=2&limit=500`) if implemented, or filter with `symbols`. |

### Performance Tips  
- The service caches the merged JSON files in memory; restart the server to refresh data.  
- For high‑traffic deployments, run behind a reverse proxy (NGINX, Traefik) and enable HTTP/2.  
- Consider deploying to a container platform (Docker, Kubernetes) for horizontal scaling.

## Reference Links or Documentation  

- Repository: https://github.com/fawazahmed0/exchange-api  
- API Documentation (auto‑generated Swagger UI): `http://localhost:3000/api-docs` (once the server is running)  
- Data Sources:  
  - `allcurrencies.min.json` – full currency list  
  - `cryptocurrencies.json` – crypto‑currency data  
  - `country.json` – country‑to‑currency mapping  
- Contribution Guidelines: see `CONTRIBUTING.md` in the repo.  

Feel free to fork, open issues, or submit pull requests to improve the service!