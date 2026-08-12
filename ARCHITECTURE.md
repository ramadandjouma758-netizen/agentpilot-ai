# AgentPilot AI — System Architecture

## 1. Architecture Goal

AgentPilot AI should use a modular architecture that is simple to develop initially and easy to scale as the product grows.

The architecture should separate:

- User interface
- Backend services
- Database
- Commerce platform integrations
- AI services
- Authentication
- Billing
- Analytics

The system should allow new commerce platforms and features to be added without rebuilding the entire application.

---

## 2. High-Level Architecture

The initial system follows this structure:

User
↓
Frontend
↓
Backend API
↓
Application Services
↓
Database

External integrations connect to the backend:

Shopify
Amazon
Other supported platforms

The AI layer connects to the backend and uses authorized application data to provide intelligent assistance.

---

## 3. Frontend

The frontend is responsible for the user interface and user experience.

Primary responsibilities:

- Display Global Leaders
- Display regional leader cards
- Display product price and sales
- Provide navigation
- Provide the Profit Calculator
- Provide authentication screens
- Display user account information
- Display AI assistant interface
- Display subscription information

The frontend should be:

- Responsive
- Mobile-first
- Fast
- Accessible
- Simple

The frontend must not directly access private databases or commerce platform credentials.

---

## 4. Backend

The backend is responsible for business logic and secure communication between the frontend, database, external platforms, and AI services.

Primary responsibilities:

- Authentication
- Authorization
- Store management
- Product data processing
- Sales data processing
- Leaderboard calculations
- Geographic classification
- Profit calculations
- AI requests
- Subscription management
- Privacy controls
- API endpoints

The backend should validate all important data before storing or displaying it.

---

## 5. Database

The database stores application data required by AgentPilot.

Initial data domains may include:

- Users
- Stores
- Products
- Sales
- Regions
- Leaderboard records
- Store permissions
- AI usage
- Subscriptions
- Payments
- Notifications

The database design should avoid unnecessary duplication.

Sensitive credentials should never be stored in plain text.

---

## 6. Commerce Platform Integrations

AgentPilot should use a modular integration architecture.

Each commerce platform should have its own integration module.

Initial planned integrations:

- Shopify
- Amazon

Future integrations may include:

- WooCommerce
- BigCommerce
- Other supported commerce platforms

Each integration should be responsible for:

- Authentication/authorization
- Retrieving permitted store data
- Retrieving permitted product data
- Retrieving permitted sales data
- Normalizing platform-specific data

The rest of AgentPilot should work with a common internal data model rather than platform-specific formats.

---

## 7. Normalized Commerce Data

Different platforms use different terminology and data structures.

AgentPilot should convert external platform data into a common internal structure.

Example:

Platform-specific data
↓
Integration Adapter
↓
Normalized Store Data
↓
AgentPilot Services

This allows Shopify and Amazon stores to participate in the same leaderboard.

---

## 8. Leaderboard Service

The Leaderboard Service calculates the regional leaders.

Basic process:

1. Retrieve authorized sales data.
2. Determine the relevant 24-hour period.
3. Calculate eligible units sold.
4. Determine the store's geographic region.
5. Compare participating stores within each region.
6. Select the highest eligible seller.
7. Store or cache the leaderboard result.
8. Return simplified data to the frontend.

Initial regions:

- North America
- South America
- Europe
- Africa
- Asia
- Australia & Oceania

The system should select one leader per region.

---

## 9. Leaderboard Data Rules

The leaderboard should expose only approved public information.

Possible public fields:

- Rank
- Medal
- Store name
- Optional display name
- Platform
- Region
- Product name
- Product price
- Units sold

Private information must remain private.

The system must never expose:

- Email addresses
- Customer information
- Private credentials
- Private store financial information

without appropriate authorization.

---

## 10. Profit Calculator Service

The calculator should initially be simple and independent from the leaderboard.

Basic calculation:

Revenue
− Product Cost
− Advertising Cost
− Shipping Cost
=
Net Profit

Profit Margin:

Net Profit ÷ Selling Price × 100

The calculator may later support:

- Platform fees
- Payment fees
- Taxes
- Additional operating costs

Advanced fields should remain optional.

---

## 11. AI Service

The AI service will provide intelligent assistance.

The backend should act as the secure intermediary between the frontend and AI provider.

Basic flow:

User
↓
Frontend
↓
Backend
↓
AI Service
↓
Backend
↓
Frontend

The AI service may eventually support:

- Store analysis
- Product analysis
- Profitability analysis
- Marketing recommendations
- Competitor insights
- Business recommendations

AI access should respect user permissions and subscription limits.

---

## 12. Authentication

Users should have secure accounts.

The authentication system should support:

- Account creation
- Login
- Logout
- Password/security management
- Session management
- Authorization

Future authentication options may include:

- Google
- Other OAuth providers

---

## 13. Subscription and Billing

The backend should separate subscription logic from the rest of the application.

Possible plans:

- Free
- Pro
- Business
- Agency

The billing system should control access to premium features.

Example:

Free
↓
Basic features

Pro
↓
Advanced analytics + AI + no ads

Business
↓
Multiple stores + advanced tools

Agency
↓
Multiple clients + advanced reporting

Exact pricing will be defined later.

---

## 14. Advertising

Advertising should be treated as a secondary revenue system.

The system should allow advertisements for eligible free users while keeping the paid experience ad-free.

Advertising must not interfere with the core user experience.

---

## 15. Security

Security is a core architectural requirement.

The system should:

- Encrypt sensitive data where appropriate.
- Protect API credentials.
- Use secure authentication.
- Validate requests.
- Apply authorization checks.
- Avoid exposing private data.
- Keep secrets outside source code.
- Use environment variables for sensitive configuration.
- Log security-relevant events appropriately.

---

## 16. API Design

The backend should expose clear API endpoints for the frontend.

Potential API groups:

/auth
/stores
/products
/sales
/leaderboard
/calculator
/ai
/subscriptions
/users

The API structure should remain modular.

---

## 17. Caching and Performance

Leaderboard data may be cached to reduce unnecessary processing.

The system should avoid requesting the same external data repeatedly when it is not necessary.

Performance should be considered from the beginning, especially for:

- Leaderboard requests
- Store synchronization
- AI requests
- Dashboard loading

---

## 18. Background Jobs

Some tasks should run asynchronously rather than blocking the user interface.

Potential background jobs:

- Store synchronization
- Sales data processing
- Leaderboard updates
- Notifications
- Report generation
- Data cleanup

This will become more important as the number of connected stores increases.

---

## 19. Error Handling

The system should handle external platform failures gracefully.

For example:

If Shopify or Amazon is temporarily unavailable:

- Do not crash the entire application.
- Record the integration error.
- Inform the user when necessary.
- Retry where appropriate.
- Keep previously valid data when possible.

---

## 20. Scalability

The architecture should allow AgentPilot to grow from a small MVP into a larger SaaS platform.

Future scaling may include:

- More backend services
- Background workers
- Distributed caching
- Database optimization
- Additional API services
- Monitoring
- Logging
- Analytics infrastructure

These should be introduced only when required.

---

## 21. Initial Technology Direction

The initial project direction may use:

Frontend:
Next.js

Backend:
FastAPI

Database:
PostgreSQL

Version control:
Git + GitHub

Development environment:
GitHub Codespaces

The exact implementation may be adjusted if technical requirements change.

---

## 22. Development Principle

The architecture should follow:

**Build simple → Validate → Measure → Improve → Scale**

Do not build complex infrastructure before the product demonstrates real usage.

The MVP should remain small, understandable, and maintainable.

---

## 23. Future Architecture

Long-term AgentPilot may evolve into:

Frontend
↓
API Gateway
↓
Application Services
├── Store Service
├── Sales Service
├── Leaderboard Service
├── Analytics Service
├── AI Service
├── Billing Service
└── Notification Service
↓
Database + Cache + Background Workers
↓
External Commerce Platforms
