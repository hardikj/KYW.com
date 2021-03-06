def index():
    return dict(message=T('Hello World'))

def map():
    form = FORM('country:',INPUT(size=20,_id="country",_name='country',requires=IS_NOT_EMPTY()),INPUT(_type='submit'))
    row = ""
    if form.accepts(request):
        response.flash="hey form accepted"
        row = db.sdata(db.sdata.country==form.vars.country)
        return dict(form=form,row=row)
    else:
        return dict(form = form,row=row)
    import pdb;pdb.set_trace()
def gmap():
    form = FORM('country:',INPUT(size=20,_id="country",_name='country',requires=IS_NOT_EMPTY()),INPUT(_type='submit'))
    row = ""
    if form.accepts(request):
        row = db.sdata(db.sdata.country==form.vars.country)
        return dict(form=form,row=row)
    else:
        return dict(form = form,row=row)
   
def ajax():
    
    msg = request.vars.q;
    msg = msg.lstrip()
    if(msg=="South Korea" ):
        msg="Korea, South"
    if(msg=="North Korea"):
        msg= "Korea, North"
    if(msg=="USA"):
        msg= "United States" 
    if(msg):
        #import pdb;pdb.set_trace()
        record = db.sdata(db.sdata.country==msg)
        #r = db.sdata(db.sdata.country==msg)
    else:
        record = "some prob here"
    return dict(r = record)     
    
    
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
