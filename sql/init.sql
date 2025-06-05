CREATE DATABASE IF NOT EXISTS mydb02_dev;
USE mydb02_dev;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- user123/pass123
INSERT INTO user (name, email, password) VALUES ('user123', 'user123@hotmail.com', '$2b$12$abcdefghijklmnopqrstuuqtksgstOHrgkSMBpr4WAH.OValZhwfa');


CREATE TABLE note (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- 笔记ID（自增主键）
    title VARCHAR(255) NOT NULL,        -- 笔记标题（不能为空）
    content TEXT,                       -- 笔记内容（文本类型）
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 创建时间（默认当前时间）
);

INSERT INTO note (title, content) VALUES ('第一个note', '内容123');

