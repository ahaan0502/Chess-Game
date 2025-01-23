CREATE TABLE game_history (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    player1_id INT,
    player2_id INT,
    moves TEXT,
    winner_id INT,
    FOREIGN KEY (player1_id) REFERENCES users(id),
    FOREIGN KEY (player2_id) REFERENCES users(id),
    FOREIGN KEY (winner_id) REFERENCES users(id)
);