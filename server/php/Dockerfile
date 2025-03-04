FROM php:8.2.11-fpm


# Install Composer
RUN echo "Install COMPOSER"
RUN cd /tmp \
    && curl -sS https://getcomposer.org/installer -o composer-setup.php \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && rm composer-setup.php


# Install required PHP extensions
RUN docker-php-ext-install pdo pdo_mysql


# Update package manager and install useful tools
RUN apt-get update && apt-get -y install apt-utils nano wget dialog vim


# Install important libraries
RUN echo "Install important libraries"
RUN apt-get -y install --fix-missing \
    apt-utils \
    build-essential \
    git \
    curl \
    libcurl4 \
    libcurl4-openssl-dev \
    zlib1g-dev \
    libzip-dev \
    zip \
    libbz2-dev \
    locales \
    libmcrypt-dev \
    libicu-dev \
    libonig-dev \
    libxml2-dev \
    nodejs \
    npm

# Reverb dependencies
RUN docker-php-ext-install pcntl
RUN docker-php-ext-configure pcntl --enable-pcntl

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Add any additional configurations or adjustments as needed


# Set the working directory
WORKDIR /var/www


# Expose the port
EXPOSE 9000


# Define the entry point
CMD ["php-fpm"]