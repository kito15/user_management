The User Management System Final Project: Your Epic Coding Adventure Awaits! 🎉✨🔥
Introduction: Buckle Up for the Ride of a Lifetime 🚀🎬
Welcome to the User Management System project - an epic open-source adventure crafted by the legendary Professor Keith Williams for his rockstar students at NJIT! 🏫👨‍🏫⭐ This project is your gateway to coding glory, providing a bulletproof foundation for a user management system that will blow your mind! 🤯 You'll bridge the gap between the realms of seasoned software pros and aspiring student developers like yourselves.

Instructor Video - Project Overview and Tips 🎥
Introduction to the system features and overview of the project - please read 📚
Project Setup Instructions ⚒️
Features to Select From 🛠️
About the Project🔥🌟
Goals and Objectives: Unlock Your Coding Superpowers 🎯🏆🌟
Get ready to ascend to new heights with this legendary project:

Practical Experience: Dive headfirst into a real-world codebase, collaborate with your teammates, and contribute to an open-source project like a seasoned pro! 💻👩‍💻🔥
Quality Assurance: Develop ninja-level skills in identifying and resolving bugs, ensuring your code quality and reliability are out of this world. 🐞🔍⚡
Test Coverage: Write additional tests to cover edge cases, error scenarios, and important functionalities - leave no stone unturned and no bug left behind! ✅🧪🕵️‍♂️
Feature Implementation: Implement a brand new, mind-blowing feature and make your epic mark on the project, following best practices for coding, testing, and documentation like a true artisan. ✨🚀🎆
Collaboration: Foster teamwork and collaboration through code reviews, issue tracking, and adhering to contribution guidelines - teamwork makes the dream work, and together you'll conquer worlds! 🤝💪🌍
Industry Readiness: Prepare for the software industry by working on a project that simulates real-world development scenarios - level up your skills to super hero status and become an unstoppable coding force! 🔝🚀🏆⚡
Submission and Grading: Your Chance to Shine 📝✏️📈
Reflection Document: Submit a 1-2 page Word document reflecting on your learnings throughout the course and your experience working on this epic project. Include links to the closed issues for the 5 QA issues, 10 NEW tests, and 1 Feature you'll be graded on. Make sure your project successfully deploys to DockerHub and include a link to your Docker repository in the document - let your work speak for itself! 📄🔗💥

Commit History: Show off your consistent hard work through your commit history like a true coding warrior. Projects with less than 10 commits will get an automatic 0 - ouch! 😬⚠️ A significant part of your project's evaluation will be based on your use of issues, commits, and following a professional development process like a boss - prove your coding prowess! 💻🔄🔥

Deployability: Broken projects that don't deploy to Dockerhub or pass all the automated tests on GitHub actions will face point deductions - nobody likes a buggy app! 🐞☠️ Show the world your flawless coding skills!

Managing the Project Workload: Stay Focused, Stay Victorious ⏱️🧠⚡
This project requires effective time management and a well-planned strategy, but fear not - you've got this! Follow these steps to ensure a successful (and sane!) project outcome:

Select a Feature: Choose a feature from the provided list of additional improvements that sparks your interest and aligns with your goals like a laser beam. ✨⭐🎯 This is your chance to shine!

Quality Assurance (QA): Thoroughly test the system's major functionalities related to your chosen feature and identify at least 5 issues or bugs like a true detective. Create GitHub issues for each identified problem, providing detailed descriptions and steps to reproduce - the more detail, the merrier! 🔍🐞🕵️‍♀️ Leave no stone unturned!

Test Coverage Improvement: Review the existing test suite and identify gaps in test coverage like a pro. Create 10 additional tests to cover edge cases, error scenarios, and important functionalities related to your chosen feature. Focus on areas such as user registration, login, authorization, and database interactions. Simulate the setup of the system as the admin user, then creating users, and updating user accounts - leave no stone unturned, no bug left behind! ✅🧪🔍🔬 Become the master of testing!

New Feature Implementation: Implement your chosen feature, following the project's coding practices and architecture like a coding ninja. Write appropriate tests to ensure your new feature is functional and reliable like a rock. Document the new feature, including its usage, configuration, and any necessary migrations - future you will thank you profusely! 🚀✨📝👩‍💻⚡ Make your mark on this project!

Maintain a Working Main Branch: Throughout the project, ensure you always have a working main branch deploying to Docker like a well-oiled machine. This will prevent any last-minute headaches and ensure a smooth submission process - no tears allowed, only triumphs! 😊🚢⚓ Stay focused, stay victorious!

Remember, it's more important to make something work reliably and be reasonably complete than to implement an overly complex feature. Focus on creating a feature that you can build upon or demonstrate in an interview setting - show off your skills like a rockstar! 💪🚀🎓

Don't forget to always have a working main branch deploying to Docker at all times. If you always have a working main branch, you will never be in jeopardy of receiving a very disappointing grade :-). Keep that main branch shining bright!

Let's embark on this epic coding adventure together and conquer the world of software engineering! You've got this, coding rockstars! 🚀🌟✨

Welcome to the User Management System, a powerful and scalable solution built using the FastAPI web framework! 🌟 This document provides a comprehensive overview of the system's architecture, key features, and implementation details. Let's dive in and explore the awesomeness! 😎

🏗️ Architecture
The User Management System follows a modular and layered architecture to ensure separation of concerns and promote maintainability and scalability. The core components include:

FastAPI Application: The main entry point of the application, handling API requests and responses.
Database Layer: Utilizes SQLAlchemy ORM for efficient database interactions and data persistence.
Alembic: Used for seamless database migrations.
Service Layer: Contains the business logic and core functionalities of the application.
API Layer: Defines the API endpoints, request validation, and response serialization.
Authentication and Authorization: Implements OAuth2 with Password Flow for secure user authentication and role-based access control.
Email Service: Handles email notifications and verification, with support for email templates.
💪 Best Practices and Standards
The project adheres to industry best practices and coding standards to ensure code quality, clarity, and maintainability:

PEP 8: Consistent code formatting for improved readability.
Type Hints: Enhances code clarity and catches potential type-related issues.
Dependency Injection: Promotes loose coupling and testability.
Asynchronous Programming: Efficient handling of concurrent requests.
Error Handling and Logging: Robust error handling and debugging capabilities.
Testing with Pytest: Comprehensive unit and integration testing.
Containerization with Docker: Seamless deployment and scalability.
🌟 Key Features
👥 User Management
✅ User registration and login functionality (needs more testing)
🔑 User roles and permissions: Admin, Manager, Authenticated, Anonymous (needs more testing)
🍞 User account management (BREAD operations)
📧 Email verification for registered user accounts
🔒 First user automatically becomes admin (to be converted to a command-line program in the future)
📜 API Design and Documentation
🌐 RESTful API endpoints for user management
📝 Swagger/OpenAPI documentation for easy API exploration and integration
🔐 Secure authentication and authorization using OAuth2 with Password Flow
🗄️ Database Integration
🐘 Integration with PostgreSQL database using SQLAlchemy ORM
⚡ Efficient and scalable database design for user management
⏩ Asynchronous database operations for improved performance
📧 Email Notifications
📬 Email templates for user verification and other notifications
🎨 Easily customizable email templates with headers and footers
🔍 Integration with Mailtrap for email testing and viewing in a test account
🧪 Testing and Quality Assurance
🔍 Comprehensive test suite for unit testing and integration testing
🔧 Fixtures for setting up test data and mocking dependencies
🚀 Continuous Integration and Continuous Deployment (CI/CD) pipeline with GitHub Actions
🚀 Deployment and Containerization
🐳 Dockerization of the application for easy deployment and scalability
📦 Docker Compose for managing multi-container setup
⚙️ GitHub Actions workflow for automated testing and deployment
🔐 Administrator User Creation
🔑 Automatic assignment of administrator role to the first user created in the system
⚠️ Implemented for development and testing purposes, to be converted to a command-line program for security
🌐 CORS Support
🔀 Basic CORS support, although not configured for a specific domain
🆕 Features to be developed and tested
🆔 Username Generation (needs more testing)
🔀 Users are assigned a random username upon creation
🌐 Username is generated based on a combination of nouns, verbs, and a number
✏️ Users can change their username, but it must be unique
🔍 Username serves as a URL-safe identifier for posts and public information
🔒 Ensures user anonymity and privacy, if desired
⚠️ Needs more testing and verification
🌟 Pro Status Upgrade (needs additional development pro status is added to the schema and has some functionality)
🆙 Users can request to upgrade to pro status
📝 Users must fill out their complete profile to be verified as a pro
🔍 Pro status will be used for various purposes in the future
🔐 Upgrade request and verification process needs to be implemented
Additional Features Required

📜 Open Source and MIT License - Here
The User Management System is open-sourced under the MIT License, allowing for free use, modification, and distribution of the codebase. By making the project open source, it encourages:

🤝 Collaboration and knowledge sharing
🌍 Community contribution and improvement
🎓 Flexibility for students and developers to learn from and build upon the project
🚀 Let's Build Something Amazing!
We hope this technical overview has given you a comprehensive understanding of the User Management System. With its robust architecture, best practices, and exciting features, it provides a solid foundation for building scalable and secure user management solutions.

Feel free to explore the codebase, contribute to the project, and unleash your creativity! If you have any questions or suggestions, don't hesitate to reach out. Happy coding! 💻✨

Fork this repository to your own account.

Clone the project repository to your local machine.

Create a local .env file with your MailTrap SMTP settings. Mailtrap allows you to view emails when you test the site manually. When running pytest, the system uses a Mock to simulate sending emails but doesn't actually send them.

Alembic and Pytest:

When you run Pytest, it deletes the user table but doesn't remove the Alembic table. This can cause Alembic to get out of sync.
To resolve this, drop the Alembic table and run the migration (docker compose exec fastapi alembic upgrade head) when you want to manually test the site through http://localhost/docs.
If you change the database schema, delete the Alembic migration, the Alembic table, and the users table. Then, regenerate the migration using the command: docker compose exec fastapi alembic revision --autogenerate -m 'initial migration'.
Since there is no real user data currently, you don't need to worry about database upgrades, but Alembic is still required to install the database tables.
Run the project:
docker compose up --build
Set up PGAdmin at localhost:5050 (see docker compose for login details)
View logs for the app: docker compose logs fastapi -f
Run tests: docker compose exec fastapi pytest
Set up the project with DockerHub deployment as in previous assignments for email testing. Enable issues in settings, create the production environment, and configure your DockerHub username and token. You don't need to add MailTrap, but if you want to, you can add the values to the production environment's variables.

🚀 Epic User Management System - Project Options
Welcome, future software engineering rock stars! 🌟 Here are some exciting project options to level up your skills and create an amazing User Management System. Each project focuses on different aspects of the system and comes with its own set of challenges and learning opportunities. Remember, the goal is to build upon the existing system and showcase your abilities in a way that aligns with the project requirements.

1. 🌄 Profile Picture Upload with Minio
Description: Enhance the user profile management functionality by allowing users to upload and store their profile pictures using Minio, a distributed object storage system.
User Story: As a user, I want to be able to upload and update my profile picture to personalize my account.
Difficulty Level: Medium
Minimum Viable Feature:
Implement an API endpoint for users to upload their profile picture.
Store the uploaded profile pictures securely in Minio.
Update the user profile API endpoints to include the profile picture URL.
Retrieve the profile picture URL from Minio when displaying user profiles.
Optional Enhancements:
Implement image resizing and optimization to ensure consistent image sizes and faster loading times.
Add validation to restrict the allowed image formats and sizes.
Provide a default profile picture for users who haven't uploaded one.
Getting Started:
Follow the Minio setup instructions: Setting up Object Storage with Minio with Docker
Review the existing user profile management code and database schema.
Create a new API endpoint for profile picture upload, handling file uploads and storage in Minio.
Update the user profile model and database schema to include a field for the profile picture URL.
Write unit tests to verify the profile picture upload and retrieval functionality.
2. 📧 Event-Driven Email Notifications with Celery and Kafka
Description: Refactor the email notification system to use event processing with Celery as the task queue and Kafka as the message broker. This will enable efficient and scalable handling of various email notification events.
User Story: As a user, I want to receive timely email notifications for important events such as account verification, account locking/unlocking, role upgrades, and professional status upgrades.
Difficulty Level: High
Minimum Viable Feature:
Refactor the existing email notification code to use Celery tasks for sending emails asynchronously.
Set up Kafka as the message broker for reliable and scalable event processing.
Define event types for account verification, account locking/unlocking, role upgrades, and professional status upgrades.
Implement Celery tasks to handle each event type and send the corresponding email notifications.
Optional Enhancements:
Implement retry mechanisms for failed email deliveries.
Add monitoring and logging for the event processing pipeline.
Optimize the email templates for better performance and maintainability.
Getting Started:
Read the article on Leveraging Celery and Kafka for Efficient Distributed Processing in Python to understand the concepts and architecture.
Set up Celery and Kafka in your development environment.
Refactor the existing email notification code to use Celery tasks.
Define Kafka topics for each event type and configure Celery to consume messages from these topics.
Implement the Celery tasks to handle each event type and send the corresponding email notifications.
Write unit tests to verify the event processing and email notification functionality.
3. 🔍 User Search and Filtering
Description: Implement search and filtering capabilities to allow administrators to easily find and manage users based on various criteria.
User Story: As an administrator, I want to be able to search for users based on their username, email, role, or other relevant attributes and filter the user list accordingly.
Difficulty Level: Medium
Minimum Viable Feature:
Add search functionality to allow administrators to search for users by username, email, or role.
Implement filtering options to allow administrators to filter users based on criteria like account status or registration date range.
Update the user management API endpoints to support search and filtering.
Optional Enhancements:
Implement advanced search using full-text search or ElasticSearch integration.
Add pagination and sorting options to the user search results.
Provide a user-friendly interface for administrators to perform user search and filtering.
Getting Started:
Review the existing user management code and API endpoints.
Design and implement the search and filtering functionality, considering the search criteria and filtering options.
Update the user management API endpoints to accept search and filtering parameters.
Write unit tests to verify the user search and filtering functionality.
4. 🔑 RBAC Enhancements
Description: Enhance the existing Role-Based Access Control (RBAC) system to allow administrators to change user roles dynamically.
User Story: As an administrator, I want to be able to change user roles from Authenticated to Manager or Admin, and vice versa, to manage user permissions effectively.
Difficulty Level: Medium
Minimum Viable Feature:
Implement API endpoints for administrators to change user roles.
Ensure that role changes are properly validated and propagated throughout the system.
Log all role changes for auditing purposes.
Optional Enhancements:
Add an event publisher a role is changed.
Getting Started:
Review the existing RBAC implementation in the codebase.
Design the API endpoints and request/response schemas for role management.
Implement the role change functionality in the user management service.
Write unit tests to verify the role change functionality and permission propagation.
5. 🎉 Event Management with BREAD Functionality
Description: Implement a comprehensive event management system with full BREAD (Browse, Read, Edit, Add, Delete) functionality, allowing managers and admins to create and manage events.
User Story: As a manager or admin, I want to be able to create, view, update, and delete events, including details such as start and end dates, event creator, and other relevant fields.
Difficulty Level: High
Minimum Viable Feature:
Implement API endpoints for event management with BREAD operations.
Create database models and schemas for storing event information.
Implement authorization checks to ensure only managers and admins can create and manage events.
Optional Enhancements:
Implement event registration functionality for users to sign up for events.
Add event categories and tags for better organization and searchability.
Implement event reminders and notifications for registered users.
Getting Started:
Design the database schema for storing event information, including fields like start date, end date, event creator, and other relevant details.
Implement the API endpoints for event management, handling BREAD operations.
Create the necessary database models and ORM mappings for events.
Implement authorization checks in the API endpoints to restrict access based on user roles.
Develop the frontend interface for event management, integrating with the API endpoints.
Write unit tests to verify the event management functionality, including BREAD operations and authorization checks.
6. 🌐 Localization Support
Description: Implement localization support to allow the application to be easily translated into multiple languages.

User Story: As a user, I want to be able to use the application in my preferred language.

Difficulty Level: Medium

Minimum Viable Feature:

Add localization support to the application, allowing for easy translation of user-facing text.
Research how to best handle localization for content translation of api responses and request handling.
Implement a way for users to switch between available languages.
Research best practices in handling timezones
Optional Enhancements:

Support dynamic language switching without requiring a page reload.
Implement language fallback mechanism to handle missing translations gracefully.
Getting Started:

Research and choose a localization library or framework that integrates well with your application.
Define the supported languages and create language resource files for each language.
Implement language switching functionality, allowing users to change their preferred language.
Update the application code to use the localized text from the language resource files.
Write unit tests to verify the localization functionality.
7. 📊 User Retention Analytics
Description: Implement user retention analytics to track and analyze user engagement and retention within the application.

User Story: As an administrator, I want to gain insights into user retention, user invitations, and conversion rates from anonymous to authenticated users.

Difficulty Level: Medium

Minimum Viable Feature:

Track the number of anonymous users requesting published content.
Monitor the conversion rate of anonymous users becoming authenticated users.
Analyze user login activity to identify users who haven't logged in for 24 hours, 48 hours, 1 week, or 1 year.
Optional Enhancements:

Visualize user retention data through charts and graphs.
Implement cohort analysis to track user retention over time.
Provide actionable insights and recommendations based on user retention data.
Getting Started:

Review the existing user tracking and analytics code.
Implement logging mechanisms to track anonymous user activity and conversion rates.
Create database tables or use a suitable analytics service to store user retention data.
Develop queries and algorithms to analyze user login activity and identify inactive users.
Implement the user invitation functionality, including email templates and invitation tracking.
Create API endpoints to retrieve user retention analytics data.
Write unit tests to verify the accuracy and reliability of the user retention analytics.
8. 🎫 QR Code Generation User Invites with Minio
Description: Implement QR code generation functionality for user profiles, allowing users to share their profile information easily. Store the generated QR codes using Minio.
User Story: As a user, I want to be able to invite people to the site through email by inputing their name and email address..
Difficulty Level: Medium
Minimum Viable Feature:
Implement user invitation functionality through the API, allowing users to invite others to join the platform via email with a QR code in the invitation email.
Generate unique QR codes for each invite that encodes parameter for a base64 encoded nickname field (nickname exists in the db) that identifies the user that invited them, so that we can track sucessful invitations. Create a table to track invitations and their usage. When you scan the QR code, the user should just be forwarded to another address set with a setting in config.py and their QR invite should be marked accepted in the database.
Store the generated QR codes securely in Minio. Setting up Object Storage with Minio with Docker
Provide an API endpoint for QR codes to show a user the number of invites sent and used.
Provide an API endpoint to accept the invite
Use .env file for forward email
Provide a management BREAD HATEOS complete set of endpoints to administer invitations
Optional Enhancements:
Provide options to share the QR code image on social media or via email.
Getting Started:
Set up Minio for storing the generated QR code images.
Research and select a suitable QR code generation library for your programming language.
Design the QR code generation process, including the data to be encoded in the QR code (e.g., user profile URL).
Implement the QR code generation functionality, storing the generated images in Minio.
Write unit tests to verify the QR code generation, storage, and retrieval functionality.
Write tests for testing the usage of the QR code to accept the invite by simulating the incoming request and updating the QR code
WRite any additional tests to verify the BREAD HATEOS functionality similar to the Users table, but simpler.
9. 👤 User Profile Management
Description: Enhance the user profile management functionality to allow users to update their profile fields and enable managers and admins to upgrade users to professional status.
User Story: As a user, I want to be able to manage my profile information and get upgraded to professional status by managers or admins.
Difficulty Level: Easy
Minimum Viable Feature:
Implement API endpoints for users to update their profile fields, such as name, bio, location, etc.
Create a separate API endpoint for managers and admins to upgrade a user to professional status.
Update the user profile page to display the professional status and allow users to edit their profile fields.
Send notifications to users when their professional status is upgraded.
Optional Enhancements:
Implement profile field validation to ensure data integrity.
Allow users to add additional profile fields dynamically.
Provide a user-friendly interface for managers and admins to search and select users for professional status upgrade.
Getting Started:
Review the existing user profile management code and database schema.
Design the API endpoints for updating user profile fields and upgrading professional status.
Implement the necessary database updates to store professional status information.
Create the user profile update functionality, including form validation and database updates.
Develop the professional status upgrade feature for managers and admins.
Update the user profile page to display the professional status and allow profile field editing.
Write unit tests to verify the profile update and professional status upgrade functionality.
10. 🖥️ Admin Console Application
Description: Develop a console application to manage the User Management System, including features like dropping database tables, changing user roles, and uploading CSV files with user profile data.
User Story: As an administrator, I want to have a command-line interface to perform administrative tasks such as database management, user role assignment, and bulk user creation from CSV files.
Difficulty Level: High
Minimum Viable Feature:
Implement a command-line interface using a library like Click or ArgParse.
Provide commands to drop all database tables, including the Alembic table, for database reset.
Implement commands to change user roles (e.g., Authenticated to Manager or Admin).
Add functionality to upload CSV files containing user profile data and create corresponding user accounts.
Optional Enhancements:
Implement data validation and error handling for CSV file uploads.
Provide a command to export user data to a CSV file.
Add commands to manage other system settings and configurations.
Getting Started:
Choose a suitable library for creating command-line interfaces, such as Click or ArgParse.
Design the command structure and arguments for each administrative task.
Implement the database management commands, including dropping tables and resetting the database.
Create the commands for changing user roles, integrating with the existing RBAC system.
Develop the functionality to parse CSV files and create user accounts based on the provided data.
Write unit tests to verify the functionality of each command and the corresponding actions.
These project options offer a diverse range of features and enhancements to the User Management System, catering to different skill levels and interests. From profile picture upload with Minio to user retention analytics and QR code generation, these projects provide opportunities for students to explore various technologies and design patterns.

Remember to consider the existing system's capabilities and the project timeline when selecting and implementing these features. Focus on delivering a functional and well-tested minimum viable product, while also considering potential enhancements and optimizations.

When working on the projects, adhere to best practices such as:

Following the coding standards and conventions established in the existing codebase.
Writing clear and concise documentation for new features and any modifications made.
Implementing appropriate error handling, data validation, and security measures.
Conducting thorough testing, including unit tests and integration tests, to ensure the reliability and integrity of the new features.
Seeking feedback and guidance from peers and instructors to improve the implementation and overcome any challenges.
Remember, the goal is to enhance your skills, gain practical experience, and contribute meaningfully to the User Management System project. Don't hesitate to ask questions, collaborate with others, and explore new technologies and techniques along the way.

Happy coding, and may your journey be filled with valuable learning experiences! 🚀✨

🚀 The User Management System: A Cutting-Edge Learning Experience for Students
The User Management System is an incredible project that not only showcases the power of modern web development technologies but also serves as a comprehensive learning resource for students across various fields. By adhering to industry best practices, incorporating the principles of the 12-Factor App methodology, and embracing the Agile Manifesto, this project offers a realistic and immersive experience that prepares students for the challenges and demands of the professional world.

🌐 Embracing the 12-Factor App Methodology
The 12-Factor App methodology is a set of principles that guide the development of modern, scalable, and robust software applications. The User Management System embodies these principles, providing students with a deep understanding of how to build applications that are production-ready.

Codebase: The codebase is a single, centralized repository, making it easy for students to collaborate, contribute, and track changes.
Dependencies: Dependencies are explicitly declared and managed, ensuring reproducible builds and consistent deployments.
Configuration: Configuration settings are separated from the codebase, allowing for seamless environment-specific customizations.
Backing Services: The project demonstrates how to treat backing services, such as databases and email providers, as attached resources, promoting portability and scalability.
Build, Release, Run: The project follows a strict separation of build, release, and run stages, enabling continuous deployment and streamlined workflows.
Processes: The application is designed to run as one or more stateless processes, facilitating horizontal scaling and fault tolerance.
Port Binding: The project showcases how to expose services via port binding, enabling seamless integration with various hosting environments.
Concurrency: Asynchronous programming techniques are employed, ensuring efficient handling of concurrent requests and maximizing resource utilization.
Disposability: The application is designed to start up and shut down gracefully, enabling smooth deployments and facilitating resilience.
Dev/Prod Parity: The project emphasizes the importance of maintaining consistency between development, staging, and production environments, reducing the risk of inconsistencies and bugs.
Logs: Logging is implemented as an event stream, providing valuable insights into the application's behavior and facilitating monitoring and troubleshooting.
Admin Processes: The project includes administrative processes, such as database migrations and user management, enabling seamless application lifecycles. - Needs a command line app...
By adhering to these principles, students gain a deep understanding of how to build robust, scalable, and maintainable applications that are ready for the real world.

🏆 Embracing the Agile Manifesto
The User Management System is grounded in the principles of the Agile Manifesto, which prioritizes individuals and interactions, working software, customer collaboration, and responding to change. By incorporating these principles, the project provides students with a hands-on experience in agile software development practices.

Individuals and Interactions over Processes and Tools: The project emphasizes collaboration, communication, and teamwork, ensuring that students learn how to work effectively in cross-functional teams.
Working Software over Comprehensive Documentation: The focus is on delivering functional software that meets real-world requirements, teaching students the importance of iterative development and continuous delivery.
Customer Collaboration over Contract Negotiation: The project simulates customer involvement, enabling students to understand the importance of stakeholder collaboration and user-centric design.
Responding to Change over Following a Plan: The project encourages adaptability and flexibility, teaching students how to embrace change and pivot as necessary, a critical skill in today's fast-paced software development landscape.
By embracing the Agile Manifesto, students gain invaluable experience in modern software development practices, preparing them for the dynamic and ever-changing nature of the industry.

🌟 Relevance to Various Fields
The User Management System is a multifaceted project that offers valuable learning opportunities for students across various fields:

📚 Software Engineering
For software engineering students, this project serves as a comprehensive introduction to web development using FastAPI, a modern and high-performance Python web framework. Students will gain hands-on experience with industry-standard tools and technologies such as SQLAlchemy, Alembic, OAuth2, and Pytest, enabling them to build robust and secure web applications.

🧑‍💼 Project Management
The project's adherence to the Agile Manifesto and incorporation of best practices such as continuous integration and deployment (CI/CD) make it an excellent learning resource for project management students. They will gain practical experience in managing software development projects, collaborating with cross-functional teams, and adapting to changing requirements.

🔒 Security and Cybersecurity
The User Management System places a strong emphasis on security, implementing features such as secure user authentication, role-based access control, and email verification. This provides cybersecurity students with a valuable opportunity to learn about industry-standard security practices and techniques for protecting user data and ensuring application integrity.

🚢 DevOps and Site Reliability Engineering
By leveraging containerization with Docker and embracing the 12-Factor App methodology, the project offers a comprehensive learning experience for DevOps and Site Reliability Engineering students. They will gain hands-on experience with deploying, scaling, and managing applications in containerized environments, as well as understanding the principles of building reliable and resilient systems.

📊 Data Engineering
While the primary focus of the User Management System is on web development and user management, the project also incorporates database design and integration. Data engineering students can benefit from learning about efficient database design, data modeling, and data persistence using SQLAlchemy ORM.

🌍 Industry Standards and Best Practices
The User Management System is grounded in industry standards and best practices, ensuring that students receive a comprehensive and practical learning experience. By adhering to coding standards such as PEP 8 and implementing type hints, the project promotes code quality, readability, and maintainability.

Furthermore, the project incorporates robust error handling, logging, and testing practices, equipping students with the skills necessary to build reliable and maintainable software systems. The use of dependency injection and asynchronous programming techniques further reinforces modern software development practices, preparing students for the challenges they may encounter in the industry.

🚀 Unleashing Student Potential
The User Management System is a powerful learning resource that not only teaches students the technical skills required for web development but also instills in them the mindset and practices necessary for success in the software industry. By embracing industry best practices, incorporating modern methodologies, and fostering collaboration and adaptation, this project empowers students to thrive in the ever-evolving world of software development.

Whether you are a software engineering student seeking to enhance your web development skills, a project management student looking to gain practical experience in agile methodologies, or a cybersecurity student interested in learning about secure user authentication and data protection, the User Management System offers a comprehensive and engaging learning experience.

So, what are you waiting for? Dive into this exciting project, collaborate with your peers, and unleash your potential! The User Management System is not just a coding exercise; it's a gateway to the world of professional software development, where innovation, teamwork, and adaptability are the keys to success. Get ready to embark on an exhilarating journey that will equip you with the skills and knowledge to tackle real-world challenges and make a lasting impact in the industry.


Alright. So welcome to the final project. Alright. So what you're gonna need to do and what I'm gonna do here is let me get my project, and we're just gonna we're gonna go from scratch here. So your projects, GitHub, repositories, and then we got user management here.

And what you're gonna need to do, and I just wanna be clear, is that you're gonna submit this with a Word document or a Google Doc, whatever you want. This has to be a document. The document is gonna have to be 1 to 2 pages, and essentially, you just need to have, like, a little brief intro of, like, what did you learn in this course, and what you you gotta do 5 issues, 10 new tests, and one feature. So you gotta find 5 bugs somewhere. Okay?

They can be documentation bugs, usability bugs, functionality bugs, whatever. We're gonna go through and find a bug right now, and then I didn't commit this like I did last time. I made a little mistake last time, But I think this is still we got this bug in here, and we're gonna see what you have to do to go through the whole process to get started here in a minute. You got you gotta do at least 10 commits. The more, the better.

You want your commits to be clear, nice. You want this project to be able to go to an interview, show it, and everybody sees that you got professional commits and you kinda, like, got it all lined up. Well, you got your testing, your project, everything's done. And here's the thing, you're gonna wanna get this set up so that see, I have mine. The first thing we're gonna look at whenever we grade is we're gonna go here.

And if this is red, you're probably gonna get a 0 or anywhere from a 0 to 50 on the on the assignment. K? If there's less than 10 commits, it's an automatic 0. The the way this has to work is that you're using this thing called Gitflow, which we may have. Long story short, what you wanna be able to have is, you have your main branch, you have a development branch, and then you got your feature and bug branches.

Okay? The development branch is whatever you're doing your features on, whatever you're working at. Okay? That's the that's one that you can test. That's like your your your mess around branch.

Okay? Once the development branch has all its tests and it works perfect, and you know it works perfect, and all the lights go green whenever you push the development branch, then you merge it to main. From the day you start the project till the day you turn it in, you gotta make sure that that main branch goes green with with its deployments. Alright? That's like your responsibility to not break what's already given to you.

If you don't break what's already given to you, you at least gonna get a 30 or a 40 on the project. Not a 0. Okay? Like, we'll we'll give you something. But if that if that branch is red, that means the test don't pass, it don't deploy.

It's got a security problem that you didn't fix, whatever it happens to be between now and the time that the semester or the the when it's due, that's a 0, because there's no reason for that not to happen. There's no reason nothing I'm asking you to do is that unbelievably difficult, and all the code you need for most of these assignments is already in here. You just gotta reorient it, you gotta figure out how it all works, and then reapply it. And what we're gonna do now is we're gonna get the project set up, and we're gonna go through our first, like, sort of getting started. You have what I want you to do is you're gonna need to read this.

And essentially what we're gonna do, we'll look at the other things, but I want you to understand, you're gonna have to select a feature, do the quality assurance, test coverage, make sure that the feature you pick and the area of quality assurance you work on is related to your feature. So you're, like, constantly working on your feature. You know that you're gonna have to do something with user invites, let's say, that's your feature, then you're gonna wanna, like, make sure you have user sign ups working. You wanna make sure that user everybody's really gonna be doing that with use like, verifying how users work, but there's other parts about email or whatever. You're gonna wanna look into that.

So your QA and your testing, that should be all related to your project. Okay? And then your project needs its own test for, like, new features, but you wanna make sure whatever you're building on already works. Because remember, the way we think of this is we're climbing a mountain. Our tests are whenever we hook in with the ropes, so we're tied in, and then we're climbing that mountain.

And if we do we climb a little bit, do testing, hook in, make sure we're solid, then we could climb a little bit more, hook in, solid, climb a little bit more. So our our tests are really there to make sure that this program continues to work. And as we go through this, we'll we'll see where I'll I'll point out, like, areas where you might be able to get some new tests and stuff that I didn't do. Your job is to maintain the working main branch, like I said. Now, let me look at let's take a look at the overall project here.

You got your setup instructions, which you should already know. The last project the really, the point of the last project was just to get you used to debugging a little bit, just to see how it runs. This is the same project, except it's, like, got a lot of the bugs fixed and has some new features added to it. But it's basically the same project, same process. Here's our features.

Why don't you go to the ballet project, and then we'll look at the features? So as you've gone through this course, we've been learning about 12 factor app and using that sort of a structure for hitting all the different areas. So this project, for the most part, except having a a console app for administration, which is one of the projects actually to do. It has all the 12 factor, things. So we got we got a code base, we got dependency management, we got configures and ENVs, we got backing services, we got a build release run cycle, we have, stateless processes, we got port binding, we got asynchronous programming, our application can start up and blah blah blah.

We got dev devprod parity, We got logging. We got we don't have admin processes yet. We do for through the API, but we don't have a dedicated command line command line, utility. So this is like, it's not a perfect app, but it hits all the professional areas of application development. You should feel proud about showing this project to people.

This is better this is this is a pretty good demonstration and being able to work on this is real solid. So then we are also looking at the Agile Manifesto. And then these are how this project is relevant to different fields of of computer security, project management, software engineering. Alright? Now, we also have, just to understand this, system features.

So this is especially useful for you if you have to explain this project to somebody on an interview, like what did you do, what what did you work on to understand this, because it's a it's a lot to say. This describes all of the functionality of the project. So you and all the features. So you got the architecture using a service layer, API layer, authentication authorization, email processing. You got PEP 8 coding standards, type hints, dependency injection, asynchronous programming, air handling and logging, testing, containerization with doctor.

We got industry standard best practices used in the application. These are all the features, user management, API, database integration with Postgres, SQL Alchemy, email notifications, testing and quality assurance process, you got your deployment, your administration administrator user creation, you got cores, then here are some features that are developed and tested and some notes on them. And but these are partially developed features, but they're like important to know because you've got username generation, a pro status feature that's partially implemented. Then this is, just so everybody is clear, this project is has a license attached to it, so it has an MIT open source license. This means that this project can be used for anything.

This can be used for commercial use, your use, anybody's use. This is completely free and clear for everybody to use for anything you want. Alright? That's useful because, actually, if you had to make any sort of other functionality, you're gonna need to have user setup, registration, some way to deploy. You're gonna need to have like, everybody who would wanna have an application needs to have these features.

Like and and and this is actually a complicated part of the program to to make to make sure that it's relatively secure and it it all works, and it does everything that it needs to do. And this that's what this does. Not perfect, but it's it's better than nothing. Alright. So the big main event for you is gonna be like, you're gonna have to do the QA and the, testing, and that's sort of like your warm up to get familiar with the code base to understand how everything works so that you can then pick one of these features, which you should pick the feature you're gonna do or at least have some feature in mind.

And I just wanna go over what these features do and just to give you little tips on it. So one is to have user profile photos and using this system called Mini. Io. And there's an article about this, but this is a neat system. Essentially, you know how you have, like, Amazon Web Services, different cloud hosting providers.

And all those cloud hosting providers provide their own implementation of how they store data, how they have, like, object what they call object storage to store files. I just think when we talk about object, we're talking about files. So Mini IO is a distributed object store. And a long story short, what it is essentially, if you develop your application with Mini IO, your application can store files in Mini. Io, and then Mini.

Io gets installed into Amazon or gets installed into Azure. So like, rather than making your application's file storage functionality, dependent upon a specific vendor like Amazon or Azure. If you do Mini IO, you can develop it locally, and then you can deploy it to Amazon or Azure, and then you don't and then you could connect Mini IO to their storage systems, and then it it abstracts the usage of those systems so that you don't have your application dependent on where you're gonna host it. So you could host it on your DigitalOcean server, move it to Amazon, move it to Azure. As long as you're not using the file system, you're ended up and you saw with the QR code, there were problems with the API hosting files on the local system.

And you can't really do that in reality because of the fact that the containers start up and it's the image that runs, and then the image doesn't save any files, and you wanna have the application portable. So Mini. Io is sort of the industry one of the industry standards for storing files with a distributed system where you don't have your file stores locked to the operating system or don't have it locked to the vendor. Okay? It's actually really relatively easy.

It's not it's it's there's libraries to do this. It's pretty neat. So that's one feature. You can implement event driven email notifications with Celery and Kafka. So, essentially, what this means is you right now, we send the email directly.

You'll see this in a minute when we do the demo. We send emails directly out of the system, and that's a problem because you really need to use a queue, for sending emails because of asynchronous operations. You don't wanna have your API waiting for an email to send or an email theft issue. You gotta have it sent through a queue, and that's what this is about. K?

So adding a message queue. Celery is a Python library. So Celery abstracts the usage of a queue, and it either can use Redis or RabbitMQ. And so Celery is the standard library in Python to be able to run run queues. And so you should look into how Celery works.

And then I've mentioned Kafka maybe. And Kafka can be used with this and it's, real time streaming data. Like, if you whenever you see things like your Uber Eats driver and you can see him coming to you and see all this, you know, live interactions. Also for AI applications, Kafka is the, plumbing that sends data in big applications. It would it's what makes microservices work.

It it's, a major thing. Like, you're you're when you go in your bank and you send money through Zelle, that money's going through Kafka. Like, Kafka's part of their infrastructure. This is big time infrastructure. It's not hard.

It's just that's the technologies that they use. So you can do user user search and filtering. So it's basically developing different ways to search and filter, retrieval of users for different places because, like, if you have a UI, you might wanna have auto completes, you might wanna have, the ability to find users, you might wanna have this type of functionality. So that's, and I and each one of these projects, some of them are a little bit easier, some are a little bit harder. RBAC is role based access controls, and so this project, it's got, one of the big differences between the old one and the new one.

This has user roles, anonymous, authenticated, manager, and admin. And so this project is a medium level project just to help deal with changing user roles and role role management. And then this is adding a new table using event management. So this would be doing bread, sort of like what we do on user records, but doing bread for, events. So we would have browse, retrieve, edit, add, delete events.

Administrators and managers could edit the events. The idea is that, people upgraded to professional status. If you have professional status, you'd be able to create an event, and then it would be unpublished, and that's pretty much the what this feature is. There's localization projects. So this is making the system able to translate.

This is something you'd have to research. Really, I didn't talk too much. But there's technology that essentially is IAT, excuse me, is the is the key word. And there's libraries and technologies that helps you translate, let's say, the fields in your database from one language to another. Like, you you end up having, like, key value pairs of, like, the ROHA and red.

So ROHA is Spanish, and then red's English. And so the translation can say if you had a field called red, if it was red in the database, it's going to say RoHA whenever it's the person that has their browser set to, Spanish. So localization is kind of interesting. It's just it's it's so the implementation is not hard, but the research on how it works is a little bit is a little bit a bit of an, thing to do. There's user retention and analytics.

This has to do with tracking the number of anonymous users requesting published content. So you're gonna have to have something related to content that's publicly available, so you'd have to have some sort of testing about that. See, you wanna you you kinda have to think that, like, you can use tests and other ways to simulate how features work before you have things that already work. Like, you can use tests to fake things out. This is basically then it goes through in here.

Then there's QR code user invites with Mini IO. So this is a little bit rather than doing user profiles, maybe what you wanna do is generate QR codes, save them in Mini IO and attach them to the, emails, so that when someone sends an email invite like, say you'd put send somebody's email email in, and then the system's gonna send them, email notification to say, hey, come sign up here. We don't have a front end. You don't do any front end. You have to simulate this through tests.

And then when they co sign up, the the way they get to the sign up is through the through the QR code. Okay? So, like, you'd have to generate it, store the QR code in Mini. Io, retrieve it out of q Mini. Io for putting it into the email whenever it was requested, so you'd have some it's similar to user profiles, except instead of pictures, we're doing QR codes.

Then we got share profile management. So this is my this is my feature. So user profile management is for the current user for them to be able to edit their profile fields. That's that's the cop out. That's the, alright.

That's the, Sam's feature. I'm just kidding. That's that fee it's not nothing, but it's not as hard as the other ones. That's like the, hey. I don't even wanna try, You can do this.

I'm just kidding. It's not it's not that it's that easy, but it's no. He don't get to do that one. He gets to do it if he wants to. But this is the only one that's on the easy tier.

That's on the e tier. That's the easy tier. This one actually isn't that bad, but this basically is an admin console application. And this is essentially like going back to calculator app, where but instead of having a calculator app with doing commands on, like, calculations, you'd have it sending REST API requests to the to the system. So you could have it directly access the database, and you could have it access the application through the API to be able to create a, a console app to manage it, because that's part of the 12 Factor app.

Because what you're gonna see is that the way the app is set up right now is that when you sign up, the 1st user signs up, the 1st user becomes the administrative user. And that's not exactly the way it should be, but for usage right now, that's the way it needs to be. Because we don't have a console app to manage the setup and teardown of the application and to manage it. We have to do it through the web interface to manage the database. We don't have a console app.

But like, if we had a console app, we would make it so that only user everybody that signs up through the front end, they are automatically authenticated users. They're just regular users. And then you would have the console app to be able to upgrade them to that admin role. Because you kind of have to think that you don't want to develop something that someone can break in through the web interface and destroy your system. So the way you from a security point of view, if you have sensitive information, if you have, database operations, you want to be able to do that through the console app, not through the web interface.

And so this console application would be the start in producing upgraded security for the for this application, which, you know, if you were doing a demo for on an interview, this is a great demo on an interview. It's a pretty good project. There's things that you'd have to learn about this, how to make the REST API calls, how to do it with the JWT tokens, like how that all all works. And that's your 10 projects. So you get pick one of those projects, and you got 2 weeks to go and do them.

The other one, the RBAC is pretty easy too. RBAC has a lot of testing, because, like, RBAC has not much implementation as far as the code, but it's got a lot of different things you have you would have to test for, for different trying to access different content, different, like, current user content, testing for, manager content, set testing for different things because you gotta verify that all the different parameters and edge cases of the user roles is validated. Now I'm not include just one of the things I would say is, like, I'm not including anybody's project. Like, I'm doing all the code on this project and and continuing. But if you actually have a project that turns out to be good and you wanna include it in it for the next version of this program, you can send me a pull request, and I'll work with you to integrate it because I don't know how many I'll get.

Maybe you'll get none. And I I kinda wanna make sure that anything added is exactly the way it needs to be for the way I plan on developing the system over time. But then you would actually get commits on an open source project that looks good. You'd actually get something you did continue to be used. And then, you know, that's why I I want these are the only features.

I designed these features to implement to basically not make you make much more than what's already there. Do you understand? So, like, the tests are already there, the database operations are already there. At most, you, like, have to add a new table and do a little bit more with an additional table or something. But all the all the codes you need to do stuff, 90% of it's there except, like, there's no code for Mini IO, but Mini IO is relatively it's a lie it's it's straightforward.

And you've already seen QR code, and you've seen console app. So I don't feel that there is anything in this project that is outside the scope of what most people could do. And the features are all well documented, like sort of well explained exactly what you have to do in order to do it. Alright. So let's get started.

What you're gonna need to do is come over to the repo, And then we're gonna need to fork this thing. And I already forked it and bring it and what we're gonna do, once you fork it, what you should do while you're, like, on your fork, like as soon as you fork it. Go over to settings and go to environments and make sure you have production environment, and make sure that you got your Docker Hub token, your Docker Hub username. And then you're gonna have to edit the Docker file to change where it's pushing you pushing where it's pushing to. So you got you got your environment secrets.

And then in the in the program, you have to come over to workflows. And then and then in here, you'll see that, like, where I'm pushing to, like, I'm pushing to WIS Club API. You'd have to change these to push to your repo. Okay? And then once you do this, then and it's over once you save this, then you should be able to come over to GitHub actions, and you should see that it's gonna deploy.

And if it don't deploy, fix it. And get that thing green. So that's like your first. You get that set up, that's your first, like, 40 points in the box that the application is working. Okay?

Do you understand? So once we do that, then what you're gonna need to do is you're gonna need to come over to this site called Mailtrap. Now, Mailtrap trapped me paying them money, and I'll tell you why. But, I mean, I don't mind paying them money. They have, you can only have 500 testing emails on the free account.

And what Mailtrap does is the system sends email verification emails out. So it when the user signs up, it's gonna send an email to verify the user. And when it sends that email out, it's the user has to click on it, and then they'll verify it. And then when they verify it, then they can log in. So if you it's email sign up verification process.

And in order to do this, what you end up having to do, you sign up for Mailtrap. You're gonna click a button. It's like, go over to email testing, add an inbox. Okay? You just put a name, and I already have it, like, for Gutenberg for me.

And here's my credentials. So we need to get these credentials. And once you clone the repo down to your down to you, There is a an ENV file. There's a sample, and it's got the maltrap info up here. But then you're gonna have to put your username and password, and then just rename it from dotenv to dotenv like, from dotenv sample to dotenv.

And then it's gonna use your settings in here in the application. I bet you whenever you first started hearing about dotenv files, you were like, what is this for? And you're you're like using them all the time now. So once we do this, then we should be able to do docker compose. So I'm gonna do a docker compose down.

I wanna make sure Docker make sure everything stopped. And then we do Docker Compose up dash dash build, and then I'm gonna do a dash d. And you don't have to, but dash d, all I wanna do is really just get it to start. And then what the dash d does is it runs it in the background. So this is all gonna go away once it starts up.

And what I'm gonna need to do is I'll do a docker compose logs fast API, and you can do a dash f, and dash f will force it to stay in the foreground so that the logs will continuously for the fast API app, they'll continuously update here, and then you have to do a control c to get out of there. If you do a docker if you do compose logs fast API without the f, then it just runs and then comes back to the it gives you back, to the foreground. It it gives you back control. Because, like, a lot of times, like, I'm when I'm developing, I'll just leave it like this where it's live. So I could just because I don't wanna see all the Nginx and all this other stuff.

I don't need that. I just wanna see the logging messages from my fast API application. That's how I target that specific app with the logs. I I say Docker Compose logs, name of the service, and then I'm gonna get the service. And if I wanna have it streaming, like where it's live in front of me all the time, then I do the dash f to put it make it foreground, and that forces it to stay open.

And then usually what I have to do is I have to open up another prompt, and I'm gonna do a Docker, compose, exec fast API, and then we're gonna do an Alembic upgrade or do it do I actually do a pie test? And remember, like you're climbing a mountain, the tests are how you hook yourself into the for climbing so you don't fall on your face. We wanna make sure that everything is working before we start working. Okay? You understand?

Like, because we're only gonna make one change and then make it sure it worked. One change, make sure it works. Once we have this, we know all our tests pass, then we're gonna wanna do it a man a manual QA of the actual application. And what we're gonna need to do to make sure that works is we're gonna need to go to local host, first 5050, and then admin password. And you might have to set up your pgadmin with the server and everything like last time, but we're gonna wanna go down to tables and wanna check what tables we have.

Because if we have that Alembic table already in there for some reason, we gotta delete it. Like, you only want that Alembic table in there essentially whenever you're gonna be really using the application, because the Alembic table keeps track of the versions of the database that have been applied. But because your database versioning is actually you don't have live user data and your database versioning is tracked by code, it's already in the Alembic code to do these things, you can safely always delete that Alembic table. And a lot of times, you'll have to delete the Alembic table, because you change schemas, you wanna regenerate stuff. You you it won't properly install again if you have that Alembic table.

Like, if we run pytest, like, for instance instance, if I do tables and then I'm gonna run Docker Compose EXE Alembic upgrade head. What I wanna see is 3 lines, and I wanna say running the initial migration. And then what would happen is is that if we come in here, we're gonna end up with tables, and then we're gonna end up with in types, You're gonna end up with what's called see, user role in there is defined in our code is what's called an enum field. And essentially what these enum fields are are if I look at this user role, it's it's part of the database, and what this does is it enforces that in the database, in the table, we have a role table. And the way the role table is set up says the database is gonna fail, like it's gonna give an error if a role is assigned to a user other than one of these roles.

So this is like a constraint on at the database level, which is like your ultimate security. That on the database layer, it's constrained to only have these fields. This is automatically set up. That's the the enum field is inside the models file. Now we have a user's table, and let's take a look at this because this is where like a lot of your key a's gonna be.

We wanna look at it, and we have a bunch of fields. And let's go and create a user. Let's create our first user. If we ran pytest, and I'm I'm what would happen is that the users table would be destroyed. The Alembic table would still be there.

The next time we wanted to manually test, we're gonna have to delete the Alembic table. Well, I'll do this right now because this trips people up, because this is gonna be what stumps people. Is if I do this if I run pytest, look what happens. See, pytest actually tests with the real database. Alright?

And I was lazy, but it's it's not as easy to fix this as it seems. I have I use the same database for testing as production because I don't wanna make an SQL script that when SQL alchemy starts up that it creates a test database. Because, like, once the test run, if we refresh our user table, we don't have a user table anymore. It's gone, but we still have that Alembic table. Because the pytest drops pytest doesn't know nothing about Alembic.

And pytest drops the user table because every time a test runs, it runs through the whole database operation. Create a database, insert users, perform the rec records because the database tests are done in isolation. So when the tests are over, the last test deletes the database. So it's dropped, so you don't have this. So if you wanna go to do manual testing, you have to go right click the Alembic table and delete it again manually.

And then we could run Alembic upgrade head, and we would get all 3 messages. If we did this without doing that, we would only get 2 messages. It wouldn't upgrade the table because the migration would be the in that Alembic table would it would say, oh, you've already run this migration. I don't need to do it again. But it didn't.

The table is not there, so it just gets jacked up because of the mismatch between testing and production. The this is one of the reasons one of the other things, like, in that command line part of the project, like, that's one of the things to do is, like, to make it so that we have a command. So we don't have to keep coming into the pgAdmin and dropping that Alembic table. We'd wanna have a command that, like, we run on the Python reset, like, command line, blah blah blah, reset database or something. Anyway, the once we do this, then the next thing that we're gonna do is let's go to the web UI and, like, let's do QA, because we're gonna find a bug, hopefully, which I'm pretty sure we will.

So this has some changes. So the user management routes require admin or managerial roles. And now we have a register route and a login. And what happens is is let's try this out. So we're gonna try it, and then I'm gonna send this And, actually, let me let me reset this.

So I already fixed this, so I'm gonna do a git stash. And, like, as long as I'm doing the user testing, all I have to do, like or doing a front end testing or maybe manual testing. Let me see the where is my? Oh, there it is. I need pgadmin.

So I would press the to view this, and I would see these records. And once we have this, then what we're looking for let let's just take a look at all the fields. So here is the unique ID. This is the user identifier. That's the primary key.

The nickname is automatically generated. Right? So there's a function in there to automatically generate nicknames. As far as like the way I want this to run is I don't want to ever show people's emails. Because my eventual intent is to have a system that has for event management and, like, students and professionals to connect.

I don't want professional emails or anybody in the professional world to have, like, their contact information openly exposed. Because, like, imagine, like, you had thousands of students all peppering you for, like, jobs. That would be annoying. So I wanna make the site protect user privacy. And so anytime we'd have to show a user, like, any sort of identifier for a user publicly, we would use their nickname.

The nickname can be changed. The email can be changed. Anybody can change any field. It won't break things. The primary key that is used to identify users is here.

And then the email is what they use to log in. And then we have first name, last name, bio, profile pictures. The user the first user got assigned the admin role, then it's this guy hasn't been marked as professional per if you mark in professional, there's a method actually already on the model to use to mark for professional, and it will do true and it'll put a time stamp on when that happened. The the mark as professional is not a system role, but we're gonna use that so that, in the future, people will be able to become professionals, and then professionals will be able to create events, but they'll be unpublished. And basically, the manager role will be able to publish events.

Like, they'll be able to publish content as the manager. But, any person who becomes a professional member of the site, they would be able to create events. Then you have last login, failed login attempts, because if you do more than 5 login attempts, it'll lock the account. There's created at, updated at, then we got our verification token. So the verification token, if we go over to SendGrid I mean, sorry, not SendGrid, but Mailtrap, what should happen is is that we end up with the the mail token.

And so it says, hello, John. Thank you for registering for our site. And then it looks like we can click on verify email, and then the email should be successfully verified. And then if we look in our database so like every time you do an operation, you're gonna wanna look in the actual physical database record to see what happened. So if we have to refresh this, it's not live.

We have to press play. So once this was done, what we're looking for is that email verified equals true, verification token is removed, and then this this guy is ready for duty. The its account's not locked. It's all ready to go. So the next thing that we're gonna wanna do is come over to authorization and let me get let's actually do it down here.

So I'll show you. So we did the register and we got John Doe at example.com. And let's do a John Doe 3 or 4 and do a Steve. And I'll run this until it works. And let's come over to pgAdmin just to see what the second user looks like.

So the second user is John Doe 4, and it's Steve Doe here. And what you'll notice is that they have a verification token and they're set to false and that their their role is anonymous, but we have a problem. You see, we have our admin is now being turned to authenticated. That's a problem, because authenticated users aren't gonna be able to test the API. So that's one of your bugs.

Do you understand why? We'll look at how this exact like, how the login and registration works in detail, and you'll be able to see how to fix this. We'll look into fixing it right now. So this guy is anonymous. If I come over to Mailtrap, what I'm gonna do is I'm gonna click on verify email.

And we got another problem because this guy, he doesn't have a a unique identifier where it says none. If you look into an email or a URL and it says none, that means that something didn't get retrieved from the database. Like it didn't you did this in fact, this none means that the user ID didn't get retrieved from the database. So we got 2 bugs right now. So if we go in here, if we clicked on the email we still have let's see what happens here.

So we can't verify this guy. So we got 2 problems. 1, the the token, the when the token is validated, the administrative role is removed from the user. So you would write that in steps, like the steps what they call steps to reproduce. You would write down the steps that you take in order to re to imp like, what did you do to cause this bug?

That's what you would write up for your issue, like steps to replace, and then this is the resolute then you would do resolution. You may wanna have, like like, we got 2 bugs to fix. Let's see how we can fix them. So let's go over the code, and we're gonna trace through the whole registration and creation process so you understand it in detail. So we go over and we have our routes.

We have a register route. And so what happens in this is register user service. Register user service. I don't actually this is a tip, and this is like something I I'm gonna probably fix myself. I don't actually like this because I think all my registration logic should be here.

And right now, I have all my registration logic in a generic create method, because this is just the generic create users. And right now, this is the only way we're creating users. But in the future, like, if you were gonna do, invitations or other types of onboarding strategies, we would wanna have different methods of like, different methods for different ways to put people in because it would depend on how we would create it. But right now, we just do create. And so let's look at how this whole process works.

So first happens is that the user gets created, it dumps the model. So this is validating that all the data matches what's required in this user create py PyDantic model. So that it at least has to have an email and a password whenever it comes in. Then Let me just get rid of some of this. So it validates the data.

Then what we gotta do is we gotta make sure that the user is not in the database, because if the user is in the database, that means they're already registered. We can't register. And let me just open up because we're gonna look at routes and services at the same time. So the logic here, just to explain, like, if you have to do something like this, is we check if the user if if this doesn't return anything, this is returning back sorry. What happens is is that if you can't find a user, then we log the message and then we return none, so the function exits.

But the none keyword the none return comes back, and look at how the user route works. The user awaits the user to come in here, but if there's no user in here, there's look at this. If there's no user in here, then it's gonna return back a 400, and it's gonna say email already exists because that's why, like, we're only gonna return back a valid user if there's a valid user to return. But if there's no valid user return, then the reason why there's no valid user is usually because the email already exists, and that's the first check that we have. So a good like a normal procedure see, you want your services designed so that they're like an abstraction between your database and your routes.

Because you wanna be able to use your services in command line applications, you wanna be able to use your services in other programs, and you don't want what the output of the program is, like REST API calls, to be tied in with your database operations, and you wanna be able to have business operations organized into your service. So that's like your translator between different things. It's like the middleman. The service is like the middleman between everybody so that you can have, like, your business operations. And if you need to change what database, how it does it, you don't have to change the business operation.

You can just change the database. Or if you wanna change your front end, you can change your front end, but you don't have to go into your service and change how it works. You want the service to essentially be neutral. It's like neutral to the database and neutral to how it does. And you return things out of the service like none so that the caller knows that something didn't work, and then it can test if there's nothing there and then do whatever it needs to do.

So we pass this check, then the validated data, we're gonna hash the password, Then we're gonna create a new user. We're gonna generate a nickname. We could look at the net generate nickname function. So this just takes a random number between 1 and a 1000 and then randomly combines one of these value 2 of these values to create the nickname. Then what happens is is this is like a almost like an if statement.

It's not an if statement, but it kinda like acts like this, is we keep looking to see if we have existing nicknames, and it'll keep regenerating fake nicknames until it gets one that's not in the database already. And then it uses that as the nickname so you don't have duplicated nicknames, because nicknames have to be unique. Then we have I just log out for debugging purposes just to say the user has been created. Here, we're gonna count, and this is where we're our admin logics come in into play. So like what's happening here is that if this is called a ternary operator, this is a a ternary is a one line if statement.

So new user equals user admin if user account equals 0, else user is anonymous. So this is what is determined that if there's no users in the database, this means this is the first person signing up, so they gotta be admin. Because if they're not admin, they're not gonna be able to administer or test through the API. This would be like if you were installing WordPress or Drupal or you had a web based install. Somebody can't go into database.

You wanna have it just be able to install and make them the admin. So this is like the check that makes that happen. If we were gonna have a console app, we might wanna change this so that we can bypass this normal this form of user creation and have a special way that we create admin users just for the command line. But, anyway, if the new user role is the admin, then the new user is email verified, because what we're gonna do is we're gonna generate a verification token for non admin users, and then we're gonna send the verification email. So, essentially, admin users, we're not really worried about sending verification emails because they're admin users.

Like, they don't need to verify. They're installing the thing. So what happens here is this has a pretty slick system, so let's just look at email sending. So the way this works is if you look at the email, it actually has like, hello, Steve. Thank you for registering.

Okay. But in the if I look at the email here, it's failing and the link is none. So this actually should be the user ID, but it's not sticking the user ID in the URL for some reason. Okay? So there's some reason usually if I see none, it means it didn't find it didn't get set, it didn't find a user, or something wrong with the way this is email is being generated.

So what we wanna do here is our We have to look at that. What's happening is is that the user comes in, then the user ID gets put into the URL. Then we call this method send e send the user email. In this method, this is pretty slick. So all you have to do to create new different types of emails is you have to have a calling function, like call that type of email, and that function has to prepare the data that's gonna be inserted into the email, and it has to pick what template it is.

But your templates, you have a folder called email templates. Where is my email templates? And so you just have markdown, and wherever the curly braces are, that's where your variables will get inserted. So you can have custom emails with the insertion of the values into the variables. And then you have your footer and header.

So this is actually whenever these emails are assembled, the footer and the header go on them and then the content goes in the middle And so you get, like, nice fancy emails that you can have any kind of email you want. You just have to make new email templates. Like, new calling functions with new data and new email templates, but the thing works like a charm. So let's go back to my what's happening here. So we're doing create and then, so here we got a problem.

So here's why our we don't we're not getting a new user ID. See, we're sending the verification email here, but we're adding the user to the database here, and then this is saving the changes. The way the database works is that the primary key, that GUID field, is not generated for the user until their record is saved. So in this workflow, there's no there's no user ID because the user ID doesn't get generated until after this line. So what we'd wanna do is take this, move it down here, save it.

Now let's test it. So in order to test it, we're gonna we don't actually need to reset the database because we we just want off the anonymous users. We just need another dude. So we'll go over to the application. And so we're gonna have to have a John Doe 44, Execute.

Then let's go over the database and see if see what we got. So we're gonna have John Doe 44. John Doe 44 should have a verification token, not verified, and let's go see what the email says. And let's hover over here and we'll see the link. And lo and behold, we now have we'll click on this, and then the email is successfully verified.

And that if you look at it, we have the user ID up in the field up here. And then you have the verification token that you're decoding up here. Slack. So once this is done, then what I would do is you should write tests that replicate that process. So that's kinda like your testing.

When I said like doing 10 tests, you find a bug like this. This bug would prevent you from doing your projects. So this is gonna be the first one that you I'm not gonna push these changes. You're gonna see that there's other bugs in what the project that you have that I I fixed in the last time, but I'm not pushing them. Like, you're you're gonna you're gonna see that there's one even before this.

But that process of looking into doing the action, look in the database, look how it is, go to where the code is, follow the the process, and then logically figure out how that what's actually happening to cause the problem. The program really doesn't do that much, but it does it pretty good the way it does it. So you got your email verification, you got the user creation, the admin, the RBAC. So you basically have to trace through, and then once you get done with that, then what you'd wanna do is come back, and we're gonna, if I log in with this, we can try to log in with one of the users. So we're gonna get John Doe, and then And then the login works on John Doe.

The next thing you're gonna wanna check is what the token says just to know this. So the JWT token I don't know if I already did this, but you gotta throw that in here. And then this will show you what the token actually encodes. So you put the token in here, and then you can see that we're our user is John Doe, and then John Doe has the authenticated role. We got another problem because John Doe, whenever he does he he's, being verified, he's getting marked as authenticated instead of admin.

That's our other problem. So what we're gonna need to do now is let's go fix that real quick. So what we probably wanna do is we wanna look at the route for verify email. So the route verify email, we get the user ID token, verify the user email, then let's go through and look at this email verified. Do you see this problem?

Because it's automatically doing role authenticated. Let's swap this out. Let's do if user dot role equals user. And I think we can do Or, actually, we do equals I'm just trying to make the lightest check here. Just let's let's see logically.

So when the user signs up, if we do in pgAdmin, when that guy signed up, they were marked as anonymous. Okay? So these were signed up and they weren't verified. So when the user signs up before their email confirmed, we keep them as anonymous because they're not real yet. They don't have they have they don't have a full account that we wanna, like we we wanna differentiate between people that have done con confirmations and have anonymous functionality.

Here, we're saying, if the user's role is anonymous, then upgrade them to authenticated so that if a role would happen to be admin or manager or something else, whatever it happened to be, that it's not gonna bother it. So it won't change so it's only gonna change the role if the role is anonymous, meaning it's a generic, nobody user signing up. Then it would change it to authenticated, and now we're gonna get the proper process. So once we once we sign this up, then let's go and try one more person. So we're just come up to here and then I'll do John 4443.

Execute. It runs. Just double check what's the database say. So we got another person. We got another verification token.

Oh, wait a second. So who we have here? Yeah. 443 is the guy we just created. So we got the verification token.

And then what we're gonna do, let's go check to the email. Do we get an email? Yes. We got an email. Email looks right.

Verifying the email. Let's do see what the database says. Now they looks like they got their verification token locked, and is authenticated. Now let's do a full test. Let's wipe out all the records so we have to delete them, and then we save the changes to wipe out.

And let's go do the whole do the whole thing. So we wanna have our first user so it's not too bad to test it. Like, once you have the process, you're just bouncing back between look at the database, look at and this is where that process happens, and then you gotta step through it and debug it. Then, like, that's front end engineering. Like, this is you know how much money you get paid to do this?

Like, a $100,000, $120,000. That's what like, the level of this type of detail is like a $100,120,000 a year job. Not your first job, but, like, if you get a hand if you get into that QA or you do junior dev, you'd maybe 2 years or so, you'll be doing this kind of work, and then this is this is what you do. I mean, it's basically, it's a pathway to being a millionaire. So what we're gonna do now is we're just gonna wrap this up, but what we gotta do let me just do a last test here.

Where is my okay. So I'm gonna do a a register. I'm a admin. Now I'm gonna look into the database. I'm gonna look and see.

Did I get an email? Yes. Okay. Is the email correct? This guy doesn't have a verification token.

See, it says none. So we go back, and we just gotta look into the logic to figure out how that how to fix that. And so we just keep trying that and work that bug out. Because it's it's gonna be some logical problem, like if I go to the user service and let's just go here in my register. It's probably just that when I'm creating the user, the the verification token doesn't get generated.

So let's just take that out. And then once we do that, let's go back to the database. And sorry for going a little over, guys, but let's just finish this. So then we just go back to here. Let's see if we get this whole test.

All right. So we're going to execute it. Comes back as admin. Let's check the database. We are email verified because I think that's what on on the admin, but let's see we have verification token.

Let's see if this works okay. So if I go back to my Mailtrap, let's see that the email works. Email verify successfully, then let's go back to the database and make sure we are still an admin. We're still an admin. Good to go.

Then we would go on to the next one. Let's just do a real real quick check. Last one. So let's just go have a John Doe whatever. Check this.

Verify the email. Email verified successfully. Let's go check our database. So you should have 2 email verified, all that works on point. So this is a good project.

This process of the debugging, the database operations is something you're gonna wanna have is like, one day, you're gonna wanna know how to do this. Like, you're gonna wanna show somebody exactly how you know how to you know how to work with the database, debug this off the back end, and you know how to swim, essentially. You know, you may not be and then make those features. Like go through this debugging, fix these issues because you saw them in the video. I'm not gonna change the the code anymore.

And you'll just go through this process, and then you build your feature, and and you're good. Okay? So we're gonna shut this down.