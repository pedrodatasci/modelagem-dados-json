CREATE SCHEMA IF NOT EXISTS hardware;
SET search_path TO hardware;

-- Table of computer brands
CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Main table: each computer references a brand
CREATE TABLE computers (
    id VARCHAR(50) PRIMARY KEY,
    brand_id INTEGER NOT NULL REFERENCES brands(id) ON DELETE CASCADE,
    model VARCHAR(100) NOT NULL,
    os VARCHAR(50) NOT NULL
);

-- CPU specs per computer
CREATE TABLE cpus (
    id SERIAL PRIMARY KEY,
    computer_id VARCHAR(50) NOT NULL REFERENCES computers(id) ON DELETE CASCADE,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    cores INTEGER NOT NULL CHECK (cores > 0),
    threads INTEGER NOT NULL CHECK (threads >= cores)
);

-- Memory modules per computer
CREATE TABLE memory_modules (
    id SERIAL PRIMARY KEY,
    computer_id VARCHAR(50) NOT NULL REFERENCES computers(id) ON DELETE CASCADE,
    type VARCHAR(20) NOT NULL,
    size_gb INTEGER NOT NULL CHECK (size_gb > 0)
);

-- Storage devices per computer
CREATE TABLE storage_devices (
    id SERIAL PRIMARY KEY,
    computer_id VARCHAR(50) NOT NULL REFERENCES computers(id) ON DELETE CASCADE,
    type VARCHAR(20) NOT NULL CHECK (type IN ('SSD', 'HDD')),
    size_gb INTEGER NOT NULL CHECK (size_gb >= 0)
);

-- GPU specs per computer
CREATE TABLE gpus (
    id SERIAL PRIMARY KEY,
    computer_id VARCHAR(50) NOT NULL REFERENCES computers(id) ON DELETE CASCADE,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL
);
