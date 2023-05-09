from tasks.task import Campaign, Offercode, Channel, Segment, Project, ProjectChange
from sqlalchemy.orm import sessionmaker

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def close_session(session):
    session.close()


def handle_error(session):
    session.rollback()
    raise Exception("Database Error")

def add_campaign(session, campaign_name):
    try:
        campaign = Campaign(campaign_name=campaign_name)
        session.add(campaign)
        session.commit()
        return campaign
    except:
        handle_error(session)


def update_campaign(session, campaign_id, new_name):
    try:
        campaign = session.query(Campaign).get(campaign_id)
        if campaign:
            campaign.campaign_name = new_name
            session.commit()
            return campaign
        else:
            return None
    except:
        handle_error(session)

# Similarly, you can create functions for adding/updating Offer Codes, Channels, Segments, and Projects
def add_offercode(session, offercode_name):
    try:
        offercode = Offercode(offercode_name=offercode_name)
        session.add(offercode)
        session.commit()
        return offercode
    except:
        handle_error(session)

def update_offercode(session, offercode_id, new_name):
    try:
        offercode = session.query(Offercode).get(offercode_id)
        if offercode:
            offercode.offercode_name = new_name
            session.commit()
            return offercode
        else:
            return None
    except:
        handle_error(session)

def add_channel(session, channel_name):
    try:
        channel = Channel(channel_name=channel_name)
        session.add(channel)
        session.commit()
        return channel
    except:
        handle_error(session)

def update_channel(session, channel_id, new_name):
    try:
        channel = session.query(Channel).get(channel_id)
        if channel:
            channel.channel_name = new_name
            session.commit()
            return channel
        else:
            return None
    except:
        handle_error(session)


def add_segment(session, segment_name):
    try:
        segment = Segment(segment_name=segment_name)
        session.add(segment)
        session.commit()
        return segment
    except:
        handle_error(session)

def update_segment(session, segment_id, new_name):
    try:
        segment = session.query(Segment).get(segment_id)
        if segment:
            segment.segment_name = new_name
            session.commit()
            return segment
        else:
            return None
    except:
        handle_error(session)

def add_project(session, project_name):
    try:
        project = Project(project_name=project_name)
        session.add(project)
        session.commit()
        return project
    except:
        handle_error(session)

def update_project(session, project_id, new_name):
    try:
        project = session.query(Project).get(project_id)
        if project:
            project.project_name = new_name
            session.commit()
            return project
        else:
            return None
    except:
        handle_error(session)

def add_project_change(session, project_id, campaign_id, offercode_id, channel_id, segment_id):
    try:
        project_change = ProjectChange(project_id=project_id, campaign_id=campaign_id, offercode_id=offercode_id, channel_id=channel_id, segment_id=segment_id)
        session.add(project_change)
        session.commit()
        return project_change
    except:
        handle_error(session)

def update_project_change(session, project_change_id, project_id, campaign_id, offercode_id, channel_id, segment_id):
    try:
        project_change = session.query(ProjectChange).get(project_change_id)
        if project_change:
            project_change.project_id = project_id
            project_change.campaign_id = campaign_id
            project_change.offercode_id = offercode_id
            project_change.channel_id = channel_id
            project_change.segment_id = segment_id
            session.commit()
            return project_change
        else:
            return None
    except:
        handle_error(session)

def get_campaign(session, campaign_id):
    try:
        campaign = session.query(Campaign).get(campaign_id)
        return campaign
    except:
        handle_error(session)

def get_offercode(session, offercode_id):
    try:
        offercode = session.query(Offercode).get(offercode_id)
        return offercode
    except:
        handle_error(session)

def get_channel(session, channel_id):
    try:
        channel = session.query(Channel).get(channel_id)
        return channel
    except:
        handle_error(session)

def get_segment(session, segment_id):
    try:
        segment = session.query(Segment).get(segment_id)
        return segment
    except:
        handle_error(session)

def get_project(session, project_id):
    try:
        project = session.query(Project).get(project_id)
        return project
    except:
        handle_error(session)

def get_project_change(session, project_change_id):
    try:
        project_change = session.query(ProjectChange).get(project_change_id)
        return project_change
    except:
        handle_error(session)

