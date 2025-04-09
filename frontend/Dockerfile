
# Use Node.js as the base image
FROM node:16-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend files
COPY . .

# Build the Vue.js app
RUN npm run build

# Install and use Nginx to serve the static files
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 5173
