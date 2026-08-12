# AgentPilot AI — Database Specification

## 1. Database Purpose

The AgentPilot database stores the information required by the entire platform.

The database is shared by all major features of AgentPilot, including:

- Users
- Stores
- Products
- Sales
- Geographic regions
- Leaderboard
- Profit calculations
- AI usage
- Subscriptions
- Notifications

The platform will use one central database architecture rather than separate databases for individual features.

---

## 2. Database Technology

Initial database:

PostgreSQL

The database structure should be designed to support future growth without unnecessary complexity during the MVP stage.

---

## 3. Users

The Users table stores account information.

Potential fields:

- id
- email
- password_hash
- display_name
- country
- created_at
- updated_at
- account_status

Important rules:

- Passwords must never be stored in plain text.
- Private user information must not be exposed publicly.
- A user may connect one or more stores in the future.

---

## 4. Stores

The Stores table represents ecommerce stores connected to AgentPilot.

Potential fields:

- id
- user_id
- store_name
- platform
- country
- region_id
- public_display_name
- leaderboard_opt_in
- created_at
- updated_at
- status

A user may own multiple stores.

Each store belongs to a geographic region.

---

## 5. Commerce Platforms

The system should identify the platform used by each store.

Initial platforms:

- Shopify
- Amazon

Future platforms may include:

- WooCommerce
- BigCommerce
- Other supported platforms

The platform should be stored in a standardized form.

---

## 6. Regions

The Regions table stores the geographic areas used by the leaderboard.

Initial regions:

- North America
- South America
- Europe
- Africa
- Asia
- Australia & Oceania

Potential fields:

- id
- name
- code

The region system should be extensible.

---

## 7. Products

The Products table stores products associated with connected stores.

Potential fields:

- id
- store_id
- external_product_id
- product_name
- price
- currency
- status
- created_at
- updated_at

The external product ID allows AgentPilot to connect the product to its original commerce platform.

---

## 8. Sales

The Sales table stores normalized sales information.

Potential fields:

- id
- store_id
- product_id
- external_order_id
- quantity
- unit_price
- currency
- sold_at
- created_at

The system should normalize sales data from different platforms.

This allows Shopify and Amazon sales to be processed using the same internal structure.

---

## 9. Leaderboard

The Leaderboard system determines the leading participating store in each region.

The leaderboard is calculated using eligible sales from the defined 24-hour period.

Potential leaderboard fields:

- id
- region_id
- store_id
- product_id
- units_sold
- product_price
- rank
- period_start
- period_end
- generated_at

The system should preserve enough information to explain how a ranking was produced.

---

## 10. Leaderboard Rules

The initial ranking rule is:

Highest eligible units sold during the last 24 hours.

The system should:

1. Collect authorized sales data.
2. Normalize the sales data.
3. Calculate units sold during the period.
4. Group stores by region.
5. Rank participating stores.
6. Select the leading store for each region.
7. Return only approved public information.

The leaderboard must not claim to represent stores that are not participating or whose data is unavailable.

---

## 11. Public Leaderboard Data

The database may contain private information, but the public leaderboard should expose only approved fields.

Public fields may include:

- Rank
- Store name
- Public display name
- Platform
- Region
- Product name
- Product price
- Units sold
- Medal

Private fields must remain protected.

Examples:

- Email address
- Customer information
- Store credentials
- Private financial information

---

## 12. Leaderboard Consent

Each store should have a setting controlling public leaderboard participation.

Example:

leaderboard_opt_in = true

Only stores that have appropriately authorized public participation should appear in the public leaderboard.

---

## 13. Profit Calculator

The basic profit calculator does not require a permanent database record for every calculation.

The initial calculation can be performed directly by the application.

Basic inputs:

- Selling price
- Product cost
- Advertising cost
- Shipping cost

Basic calculation:

Net Profit =
Selling Price
− Product Cost
− Advertising Cost
− Shipping Cost

Profit Margin =
Net Profit ÷ Selling Price × 100

Future versions may optionally store calculation history for authenticated users.

---

## 14. AI Usage

The system may track AI usage to manage limits and subscriptions.

Potential fields:

- id
- user_id
- request_type
- tokens_used
- created_at

The exact implementation will depend on the selected AI provider and billing model.

---

## 15. Subscriptions

The Subscriptions table manages paid plans.

Potential fields:

- id
- user_id
- plan
- status
- start_date
- end_date
- created_at
- updated_at

Initial plans may include:

- Free
- Pro
- Business
- Agency

Exact plans and pricing will be defined later.

---

## 16. Payments

Payment records should be separated logically from subscription access.

Potential fields:

- id
- user_id
- subscription_id
- provider
- external_payment_id
- amount
- currency
- status
- created_at

Sensitive payment information should not be stored unnecessarily.

---

## 17. Notifications

Future notifications may include:

- Leaderboard changes
- Store performance alerts
- AI recommendations
- Subscription events

Potential fields:

- id
- user_id
- type
- title
- message
- read_at
- created_at

---

## 18. Relationships

Basic relationships:

User
↓
Stores
↓
Products
↓
Sales

Stores
↓
Region

User
↓
Subscriptions
↓
Payments

User
↓
AI Usage

Store + Sales + Region
↓
Leaderboard

---

## 19. Data Security

Database security is essential.

The system should:

- Protect private user data.
- Never store passwords in plain text.
- Protect external platform credentials.
- Restrict database access.
- Use environment variables for secrets.
- Apply authorization checks.
- Avoid exposing sensitive database fields through APIs.
- Maintain appropriate backups.

---

## 20. Data Integrity

The database should enforce appropriate relationships and constraints.

Examples:

- A product must belong to a store.
- A sale must reference a valid store.
- A sale should reference a valid product where applicable.
- A store must have a valid region.
- A subscription must belong to a valid user.

The system should prevent invalid or orphaned records where possible.

---

## 21. Data Synchronization

Commerce platform data may change over time.

AgentPilot should support synchronization between connected platforms and the internal database.

Synchronization may occur through:

- APIs
- Webhooks
- Scheduled background jobs

The exact synchronization strategy will depend on each commerce platform.

---

## 22. Database Performance

The database should be optimized for important queries such as:

- Recent sales
- Store performance
- Regional leaderboard calculations
- User stores
- Product performance

Indexes should be introduced where they provide measurable benefits.

The MVP should avoid premature optimization.

---

## 23. Data Retention

Historical data may be valuable for:

- Performance analysis
- Historical leaderboards
- Trend detection
- AI recommendations

However, data retention policies should be defined according to business, technical, and legal requirements.

---

## 24. MVP Database Scope

The initial database should focus on:

1. Users
2. Stores
3. Regions
4. Products
5. Sales
6. Leaderboard data
7. Subscriptions
8. Basic AI usage

Additional tables can be introduced when the corresponding features are implemented.

---

## 25. Database Principle

The database should follow the same product philosophy:

**Simple foundation → Reliable data → Controlled growth**

Do not create unnecessary tables or complexity before the corresponding product feature requires them.
