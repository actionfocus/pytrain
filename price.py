# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import wx 
import tushare as ts
import pandas as pd
import datetime
import time
import thread
 
class Frame1(wx.Frame):
    
    codelist=['601012','512660','601328']
    var_percent_criteria=10
    stopflag=False
    
    
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="Monitor",size=(800,700))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)
        self.text1=wx.TextCtrl(panel,value="List:\n",size=(600,600),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP | wx.EXPAND)
        button1=wx.Button(panel,label="start")
        sizer.Add(button1)
        self.Bind(wx.EVT_BUTTON,self.OnClick,button1)
        button2=wx.Button(panel,label="stop")
        self.Bind(wx.EVT_BUTTON,self.Stop,button2)
        sizer.Add(button2)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
    
    def monitor(self):
        while(self.stopflag==False):
            self.text1.AppendText("\n----"+self.timestamp()+"----\n")
            index=1
            for code in self.codelist:
                ex_df = self.get_stock_data(code)
                start_price=self.get_start_price(code)
                ex_df_new = self.calc_var(ex_df, start_price)
                if self.check_alert(ex_df_new) is True:
                    self.msg = self.send_msg(ex_df_new,code)
                else:
                    self.msg = str(index)+'  Alert is not triggered on stock '+code+'. '+'Logged on '+ self.timestamp()+' .'
                index = index+1
                self.text1.AppendText(self.msg+"\n")
            del index
            del ex_df
            del ex_df_new
            del code
            for cycle in range(0,60):
                time.sleep(1)
                self.text1.AppendText(".")
            self.text1.AppendText("\n") 
        self.text1.AppendText("Stopped.\n")
        
    def OnClick(self,text):
        
        self.stopflag=False
        thread.start_new_thread(self.monitor,())
        
    def remove_monitor(self):
        self.stopflag=True
        self.text1.Clear()
    
    def Stop(self,text):
        thread.start_new_thread(self.remove_monitor,())
    
    def get_stock_data(self,stockcode):
        df1=ts.get_realtime_quotes(stockcode)
        return df1
    
    def get_start_price(self,stockcode):
        df_start=ts.get_hist_data(stockcode,start='2017-06-30',end='2017-06-30')
        print df_start
        return df_start

    def calc_var(self,df2,start_price):
        df2.insert(0,'buy_price','NaN')
        df2['buy_price']=float(start_price['close'])
        df2.insert(1,'buy_var',(float(df2.price)-df2.buy_price)/float(df2.price)*100)
#        temp_var=(float(df2.price)-start_price['close'])/float(df2.price)*100
        return df2
    
    def check_alert(self,df3):
        var_value=df3.buy_var[0]
        criteria_value=self.var_percent_criteria
        if var_value<(0-criteria_value) or (var_value>criteria_value):
            alert=True
        else:
            alert=False
        return alert
    
    def send_msg(self,df4,stockcode):
        info=u'[量化平台消息]'+stockcode+' '+df4.name.iloc[0]+u'变动超出预警值，需关注。'+u'当前价为'+df4.price.iloc[0]+u', 变动比率是'+str(df4.buy_var[0])+'%.'
        return info    

    def timestamp(self):
        stamp=datetime.datetime.now().date().strftime('%Y-%m-%d')+'-'+datetime.datetime.now().time().strftime('%H-%M')
        return stamp
    

        
if __name__=="__main__":
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()
        