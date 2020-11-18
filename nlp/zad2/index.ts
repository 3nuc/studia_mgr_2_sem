import {Client} from 'pg'
const client = new Client({
  user: 'postgres',
  password: 'postgres',
  port: 5433
});

(async () => {
  await client.connect()
  console.log(await zad1Query('videos | world'))
})()

const zad1Query = async (word: string) => {
  const q = `
    SELECT paper_title, keywords,session, ts_rank(to_tsvector('moj_slownik', abstract), query) AS rank
    FROM article, to_tsquery('moj_slownik',$1::text) query
    WHERE to_tsvector('moj_slownik', abstract) @@ query 
    ORDER BY rank DESC;                   
`
  await client.query(q, [word]);
}
// const zad2Query = async (word: string) => {

// const q =
//   `
//   SELECT paper_title, abstract, ts_rank(to_tsvector('moj_slownik', abstract), query) AS rank
//   FROM article, to_tsquery('moj_slownik', $1::text) query
//   WHERE to_tsvector('moj_slownik', abstract) @@ query 
//   ORDER BY rank DESC
//   LIMIT 10;
//   `
//   await client.query(q, [word]);
// }

const zad3Query = async (word: string) => {
const q =
`
SELECT paper_title, abstract, ts_rank(to_tsvector('moj_slownik', abstract), query) AS rank
FROM article, to_tsquery('moj_slownik', $1::text) query
WHERE to_tsvector('moj_slownik', abstract) @@ query 
ORDER BY rank DESC
LIMIT 10;
`

  await client.query(q, [word]);


}