Entities API
############

.. toctree::
   :maxdepth: 4
   :caption: Namespaces

.. autosummary::
   :toctree: generated
   
Character
---------

.. py:class:: Character

   .. py:method:: from_name()

      
        Initialize an entity from a name

        :param str name:
        :param ESIClient _client:
        :param str _token:
        :return:
        

   .. py:method:: from_names()

      
        Initialize a set of entities from a list of names

        :param list *names:
        :param ESIClient _client:
        :param str _token:
        :return:
        :rtype: dict
        

   .. py:method:: get_agents_research()

      Get agents research

   .. py:method:: get_assets()

      Get character assets

   .. py:method:: get_attributes()

      Get character attributes

   .. py:method:: get_blueprints()

      Get blueprints

   .. py:method:: get_bookmarks()

      List bookmarks

   .. py:method:: get_bookmarks_folders()

      List bookmark folders

   .. py:method:: get_calendar()

      List calendar event summaries

   .. py:method:: get_calendar_event(event_id=None)

      Get an event

      :param int event_id: event_id

   .. py:method:: get_calendar_event_attendees(event_id=None)

      Get attendees

      :param int event_id: event_id

   .. py:method:: get_clones()

      Get clones

   .. py:method:: get_contacts()

      Get contacts

   .. py:method:: get_contacts_labels()

      Get contact labels

   .. py:method:: get_contracts()

      Get contracts

   .. py:method:: get_contracts_contract_bids(contract_id=None)

      Get contract bids

      :param int contract_id: contract_id

   .. py:method:: get_contracts_contract_items(contract_id=None)

      Get contract items

      :param int contract_id: contract_id

   .. py:method:: get_corporationhistory()

      Get corporation history

   .. py:method:: get_fatigue()

      Get jump fatigue

   .. py:method:: get_fittings()

      Get fittings

   .. py:method:: get_fleet()

      Get character fleet info

   .. py:method:: get_fw_stats()

      Overview of a character involved in faction warfare

   .. py:method:: get_implants()

      Get active implants

   .. py:method:: get_industry_jobs()

      List character industry jobs

   .. py:method:: get_killmails_recent()

      Get a character's recent kills and losses

   .. py:method:: get_location()

      Get character location

   .. py:method:: get_loyalty_points()

      Get loyalty points

   .. py:method:: get_mail()

      Return mail headers

   .. py:method:: get_mail_labels()

      Get mail labels and unread counts

   .. py:method:: get_mail_lists()

      Return mailing list subscriptions

   .. py:method:: get_mail_mail(mail_id=None)

      Return a mail

      :param int mail_id: mail_id

   .. py:method:: get_medals()

      Get medals

   .. py:method:: get_mining()

      Character mining ledger

   .. py:method:: get_notifications()

      Get character notifications

   .. py:method:: get_notifications_contacts()

      Get new contact notifications

   .. py:method:: get_online()

      Get character online

   .. py:method:: get_opportunities()

      Get a character's completed tasks

   .. py:method:: get_orders()

      List open orders from a character

   .. py:method:: get_orders_history()

      List historical orders by a character

   .. py:method:: get_planets()

      Get colonies

   .. py:method:: get_planets_planet(planet_id=None)

      Get colony layout

      :param int planet_id: planet_id

   .. py:method:: get_portrait()

      Get character portraits

   .. py:method:: get_roles()

      Get character corporation roles

   .. py:method:: get_search()

      Search on a string

   .. py:method:: get_ship()

      Get current ship

   .. py:method:: get_skillqueue()

      Get character's skill queue

   .. py:method:: get_skills()

      Get character skills

   .. py:method:: get_standings()

      Get standings

   .. py:method:: get_stats()

      Yearly aggregate stats

   .. py:method:: get_titles()

      Get character corporation titles

   .. py:method:: get_wallet()

      Get a character's wallet balance

   .. py:method:: get_wallet_journal()

      Get character wallet journal

   .. py:method:: get_wallet_transactions()

      Get wallet transactions

   .. py:method:: set_token()

      
        Sets the token used for calling ESI operations.

        :param str token: ESI authorization token
        :return:
        



Corporation
-----------

.. py:class:: Corporation

   .. py:method:: from_name()

      
        Initialize an entity from a name

        :param str name:
        :param ESIClient _client:
        :param str _token:
        :return:
        

   .. py:method:: from_names()

      
        Initialize a set of entities from a list of names

        :param list *names:
        :param ESIClient _client:
        :param str _token:
        :return:
        :rtype: dict
        

   .. py:method:: get_alliancehistory()

      Get alliance history

   .. py:method:: get_assets()

      Get corporation assets

   .. py:method:: get_blueprints()

      Get corporation blueprints

   .. py:method:: get_bookmarks()

      List corporation bookmarks

   .. py:method:: get_bookmarks_folders()

      List corporation bookmark folders

   .. py:method:: get_contacts()

      Get corporation contacts

   .. py:method:: get_contacts_labels()

      Get corporation contact labels

   .. py:method:: get_containers_logs()

      Get all corporation ALSC logs

   .. py:method:: get_contracts()

      Get corporation contracts

   .. py:method:: get_contracts_contract_bids(contract_id=None)

      Get corporation contract bids

      :param int contract_id: contract_id

   .. py:method:: get_contracts_contract_items(contract_id=None)

      Get corporation contract items

      :param int contract_id: contract_id

   .. py:method:: get_customs_offices()

      List corporation customs offices

   .. py:method:: get_divisions()

      Get corporation divisions

   .. py:method:: get_facilities()

      Get corporation facilities

   .. py:method:: get_fw_stats()

      Overview of a corporation involved in faction warfare

   .. py:method:: get_icons()

      Get corporation icon

   .. py:method:: get_industry_jobs()

      List corporation industry jobs

   .. py:method:: get_killmails_recent()

      Get a corporation's recent kills and losses

   .. py:method:: get_medals()

      Get corporation medals

   .. py:method:: get_medals_issued()

      Get corporation issued medals

   .. py:method:: get_members()

      Get corporation members

   .. py:method:: get_members_limit()

      Get corporation member limit

   .. py:method:: get_members_titles()

      Get corporation's members' titles

   .. py:method:: get_membertracking()

      Track corporation members

   .. py:method:: get_orders()

      List open orders from a corporation

   .. py:method:: get_orders_history()

      List historical orders from a corporation

   .. py:method:: get_roles()

      Get corporation member roles

   .. py:method:: get_roles_history()

      Get corporation member roles history

   .. py:method:: get_shareholders()

      Get corporation shareholders

   .. py:method:: get_standings()

      Get corporation standings

   .. py:method:: get_starbases()

      Get corporation starbases (POSes)

   .. py:method:: get_starbases_starbase(starbase_id=None)

      Get starbase (POS) detail

      :param int starbase_id: starbase_id

   .. py:method:: get_structures()

      Get corporation structures

   .. py:method:: get_titles()

      Get corporation titles

   .. py:method:: get_wallets()

      Returns a corporation's wallet balance

   .. py:method:: get_wallets_division_journal()

      Get corporation wallet journal

   .. py:method:: get_wallets_division_transactions()

      Get corporation wallet transactions

   .. py:method:: set_token()

      
        Sets the token used for calling ESI operations.

        :param str token: ESI authorization token
        :return:
        



Alliance
--------

.. py:class:: Alliance

   .. py:method:: from_name()

      
        Initialize an entity from a name

        :param str name:
        :param ESIClient _client:
        :param str _token:
        :return:
        

   .. py:method:: from_names()

      
        Initialize a set of entities from a list of names

        :param list *names:
        :param ESIClient _client:
        :param str _token:
        :return:
        :rtype: dict
        

   .. py:method:: get_contacts()

      Get alliance contacts

   .. py:method:: get_contacts_labels()

      Get alliance contact labels

   .. py:method:: get_corporations()

      List alliance's corporations

   .. py:method:: get_icons()

      Get alliance icon

   .. py:method:: set_token()

      
        Sets the token used for calling ESI operations.

        :param str token: ESI authorization token
        :return:
        



