CREATE table IF NOT EXISTS youtube_songs (
    song_id SERIAL PRIMARY KEY,
    title text,
    author text,
    channel text,
    link text,
    thumbnail text,
    date timestamp default NOW()
);