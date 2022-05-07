# SparrowTeam

![mCjpYHqx_400x400](https://user-images.githubusercontent.com/74766580/167264905-228f5203-72f5-49a3-a6f1-4d4cf65a76a1.png)
## [Notion](notion.so)
` Notion API ` is Notion's set of tools and instructions that allow developers to write code that communicates with Notion. Like all other APIs, there is an API reference that developers can use to build their integrations. This reference contains all the commands that developers can use in their code.
<br>
Integrations use the API to access Notion's pages, databases, and users. Integrations can connect services to Notion and build interactive experiences for users within Notion. Using the navigation on the left, you'll find details for each endpoint and type of object used in the API.
<br>
### notion sdk for js
```
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });

(async () => {
  const databaseId = '897e5a76-ae52-4b48-9fdf-e71f5945d1af';
  const response = await notion.databases.query({
    database_id: databaseId,
    filter: {
      or: [
        {
          property: 'In stock',
          checkbox: {
            equals: true,
          },
        },
        {
          property: 'Cost of next trip',
          number: {
            greater_than_or_equal_to: 2,
          },
        },
      ],
    },
    sorts: [
      {
        property: 'Last ordered',
        direction: 'ascending',
      },
    ],
  });
  console.log(response);
})();
```
### 🟢200 normal
### 🔴400 error
