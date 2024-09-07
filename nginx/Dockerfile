# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Copy custom Nginx configuration file to the container
COPY default.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the Nginx server
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
