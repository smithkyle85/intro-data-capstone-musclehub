{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query\n",
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's an example of a query that just displays some data\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                   email  gender visit_date\n",
      "0   1000        Kim    Walter   KimWalter58@gmail.com  female     7-1-17\n",
      "1   1001        Tom   Webster        TW3857@gmail.com    male     7-1-17\n",
      "2   1002     Edward     Bowen  Edward.Bowen@gmail.com    male     7-1-17\n",
      "3   1003     Marcus     Bauer  Marcus.Bauer@gmail.com    male     7-1-17\n",
      "4   1004    Roberta      Best      RB6305@hotmail.com  female     7-1-17\n"
     ]
    }
   ],
   "source": [
    "visits = sql_query (\"select * from visits where visit_date >= '7-1-17' order by visit_date asc\")\n",
    "print visits.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                   email  gender  \\\n",
      "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
      "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
      "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
      "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
      "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
      "\n",
      "  fitness_test_date  \n",
      "0        2017-07-03  \n",
      "1        2017-07-02  \n",
      "2        2017-07-01  \n",
      "3        2017-07-02  \n",
      "4        2017-07-05  \n"
     ]
    }
   ],
   "source": [
    "fts = sql_query ('''select * from fitness_tests''')\n",
    "print fts.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                    email  gender  \\\n",
      "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
      "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
      "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
      "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
      "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
      "\n",
      "  application_date  \n",
      "0       2017-08-12  \n",
      "1       2017-09-29  \n",
      "2       2017-09-15  \n",
      "3       2017-07-26  \n",
      "4       2017-07-14  \n"
     ]
    }
   ],
   "source": [
    "apps = sql_query ('''select * from applications''')\n",
    "print apps.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index first_name last_name                    email  gender purchase_date\n",
      "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
      "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
      "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
      "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
      "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24\n"
     ]
    }
   ],
   "source": [
    "purchases = sql_query ('''select * from purchases''')\n",
    "print purchases.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first_name           5004\n",
      "last_name            5004\n",
      "visit_date           5004\n",
      "fitness_test_date    2504\n",
      "application_date      575\n",
      "purchase_date         450\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "df = sql_query('''\n",
    "SELECT visits.first_name,\n",
    "       visits.last_name,\n",
    "       visits.visit_date,\n",
    "       fitness_tests.fitness_test_date,\n",
    "       applications.application_date,\n",
    "       purchases.purchase_date\n",
    "FROM visits\n",
    "LEFT JOIN fitness_tests\n",
    "    ON fitness_tests.first_name = visits.first_name\n",
    "    AND fitness_tests.last_name = visits.last_name\n",
    "    AND fitness_tests.email = visits.email\n",
    "LEFT JOIN applications\n",
    "    ON applications.first_name = visits.first_name\n",
    "    AND applications.last_name = visits.last_name\n",
    "    AND applications.email = visits.email\n",
    "LEFT JOIN purchases\n",
    "    ON purchases.first_name = visits.first_name\n",
    "    AND purchases.last_name = visits.last_name\n",
    "    AND purchases.email = visits.email\n",
    "WHERE visits.visit_date >= '7-1-17'\n",
    "''')\n",
    "print df.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name visit_date fitness_test_date application_date  \\\n",
      "0        Kim    Walter     7-1-17        2017-07-03             None   \n",
      "1        Tom   Webster     7-1-17        2017-07-02             None   \n",
      "2     Edward     Bowen     7-1-17              None       2017-07-04   \n",
      "3     Marcus     Bauer     7-1-17        2017-07-01       2017-07-03   \n",
      "4    Roberta      Best     7-1-17        2017-07-02             None   \n",
      "\n",
      "  purchase_date ab_test_group  \n",
      "0          None             A  \n",
      "1          None             A  \n",
      "2    2017-07-04             B  \n",
      "3    2017-07-05             A  \n",
      "4          None             A  \n"
     ]
    }
   ],
   "source": [
    "df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B')\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ab_test_group  first_name\n",
      "0             A        2504\n",
      "1             B        2500\n"
     ]
    }
   ],
   "source": [
    "ab_counts = df.groupby('ab_test_group').first_name.count().reset_index()\n",
    "print ab_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(ab_counts.first_name.values, labels=['A', 'B'], autopct='%0.1f%%')\n",
    "plt.axis('equal')\n",
    "plt.show()\n",
    "plt.savefig('ab_test_pie_chart.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name visit_date fitness_test_date application_date  \\\n",
      "0        Kim    Walter     7-1-17        2017-07-03             None   \n",
      "1        Tom   Webster     7-1-17        2017-07-02             None   \n",
      "2     Edward     Bowen     7-1-17              None       2017-07-04   \n",
      "3     Marcus     Bauer     7-1-17        2017-07-01       2017-07-03   \n",
      "4    Roberta      Best     7-1-17        2017-07-02             None   \n",
      "\n",
      "  purchase_date ab_test_group  is_application  \n",
      "0          None             A  No Application  \n",
      "1          None             A  No Application  \n",
      "2    2017-07-04             B     Application  \n",
      "3    2017-07-05             A     Application  \n",
      "4          None             A  No Application  \n"
     ]
    }
   ],
   "source": [
    "df['is_application'] = df.application_date.apply(lambda x: 'Application' if pd.notnull(x) else 'No Application')\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ab_test_group  is_application  first_name\n",
      "0             A     Application         250\n",
      "1             A  No Application        2254\n",
      "2             B     Application         325\n",
      "3             B  No Application        2175\n"
     ]
    }
   ],
   "source": [
    "app_counts = df.groupby(['ab_test_group', 'is_application']).first_name.count().reset_index()\n",
    "print app_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application\n",
      "0                          A          250            2254\n",
      "1                          B          325            2175\n"
     ]
    }
   ],
   "source": [
    "app_pivot = app_counts.pivot(columns='is_application', index='ab_test_group', values='first_name').reset_index()\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total\n",
      "0                          A          250            2254   2504\n",
      "1                          B          325            2175   2500\n"
     ]
    }
   ],
   "source": [
    "app_pivot['Total'] = app_pivot.Application + app_pivot['No Application']\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total  \\\n",
      "0                          A          250            2254   2504   \n",
      "1                          B          325            2175   2500   \n",
      "\n",
      "is_application  Percent with Application  \n",
      "0                                0.09984  \n",
      "1                                0.13000  \n"
     ]
    }
   ],
   "source": [
    "app_pivot['Percent with Application'] = app_pivot.Application / app_pivot.Total\n",
    "print app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0009647827600722304\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "\n",
    "contingency = [[250, 2254], [325, 2175]]\n",
    "chi2, pval, dof, expected = chi2_contingency(contingency)\n",
    "print pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name last_name visit_date fitness_test_date application_date  \\\n",
      "0        Kim    Walter     7-1-17        2017-07-03             None   \n",
      "1        Tom   Webster     7-1-17        2017-07-02             None   \n",
      "2     Edward     Bowen     7-1-17              None       2017-07-04   \n",
      "3     Marcus     Bauer     7-1-17        2017-07-01       2017-07-03   \n",
      "4    Roberta      Best     7-1-17        2017-07-02             None   \n",
      "\n",
      "  purchase_date ab_test_group  is_application   is_member  \n",
      "0          None             A  No Application  Not Member  \n",
      "1          None             A  No Application  Not Member  \n",
      "2    2017-07-04             B     Application      Member  \n",
      "3    2017-07-05             A     Application      Member  \n",
      "4          None             A  No Application  Not Member  \n"
     ]
    }
   ],
   "source": [
    "df['is_member'] = df.purchase_date.apply(lambda x: 'Member' if pd.notnull(x) else 'Not Member')\n",
    "print df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   first_name last_name visit_date fitness_test_date application_date  \\\n",
      "2      Edward     Bowen     7-1-17              None       2017-07-04   \n",
      "3      Marcus     Bauer     7-1-17        2017-07-01       2017-07-03   \n",
      "9    Salvador  Cardenas     7-1-17        2017-07-07       2017-07-06   \n",
      "11    Valerie     Munoz     7-1-17        2017-07-03       2017-07-05   \n",
      "35    Michael     Burks     7-1-17              None       2017-07-07   \n",
      "\n",
      "   purchase_date ab_test_group is_application   is_member  \n",
      "2     2017-07-04             B    Application      Member  \n",
      "3     2017-07-05             A    Application      Member  \n",
      "9           None             A    Application  Not Member  \n",
      "11    2017-07-06             A    Application      Member  \n",
      "35    2017-07-13             B    Application      Member  \n"
     ]
    }
   ],
   "source": [
    "just_apps = df[df.is_application == 'Application']\n",
    "print just_apps.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
      "0                     A     200          50    250          0.800000\n",
      "1                     B     250          75    325          0.769231\n"
     ]
    }
   ],
   "source": [
    "member_count = just_apps.groupby(['ab_test_group', 'is_member']).first_name.count().reset_index()\n",
    "member_pivot = member_count.pivot(columns='is_member', index='ab_test_group', values='first_name').reset_index()\n",
    "member_pivot['Total'] = member_pivot.Member + member_pivot['Not Member']\n",
    "member_pivot['Percent Purchase'] = member_pivot.Member / member_pivot.Total\n",
    "print member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.43258646051083327\n"
     ]
    }
   ],
   "source": [
    "contingency = [[200, 50], [250, 75]]\n",
    "chi2, pval, dof, expected = chi2_contingency(contingency)\n",
    "print pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
      "0                     A     200        2304   2504          0.079872\n",
      "1                     B     250        2250   2500          0.100000\n"
     ]
    }
   ],
   "source": [
    "final_member_count = df.groupby(['ab_test_group', 'is_member']).first_name.count().reset_index()\n",
    "final_member_pivot = final_member_count.pivot(columns='is_member', index='ab_test_group', values='first_name').reset_index()\n",
    "final_member_pivot['Total'] = final_member_pivot.Member + final_member_pivot['Not Member']\n",
    "final_member_pivot['Percent Purchase'] = final_member_pivot.Member / final_member_pivot.Total\n",
    "print final_member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.014724114645783203\n"
     ]
    }
   ],
   "source": [
    "contingency = [[200, 2304], [250, 2250]]\n",
    "chi2, pval, dof, expected = chi2_contingency(contingency)\n",
    "print pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(range(len(app_pivot)), app_pivot['Percent with Application'].values)\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.05, 0.10, 0.15, 0.20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.title('Apps Completed Dependent on Fitness Test')\n",
    "plt.show()\n",
    "plt.savefig('percent_visitors_apply.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(range(len(member_pivot)), member_pivot['Percent Purchase'].values)\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])\n",
    "ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])\n",
    "plt.title('App-to-Member Conversion Rate per Group')\n",
    "plt.show()\n",
    "plt.savefig('percent_apply_purchase.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(range(len(final_member_pivot)), final_member_pivot['Percent Purchase'].values)\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.05, 0.10, 0.15, 0.20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.title('Overall Purchase Percentages Dependent on Test Taken')\n",
    "plt.show()\n",
    "plt.savefig('percent_visitors_purchase.png')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
