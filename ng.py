# coding=utf-8
from countryinfo import CountryInfo
countryname = "vietnam"
country = CountryInfo(countryname)
def stats():
    print("STATS")
    print("AHYYHOO")
    print(country)
    subregion = country.subregion()
    print(subregion)
    kmaera = country.area()
    print(kmaera)
    popu = country.population()
    print(popu)
    capital = country.capital()
    print(capital)
    wikiarticle = country.wiki()
    print(wikiarticle)
    embedVar = discord.Embed(title="Country info", description=country, color=0x00ff00)
    embedVar.add_field(name="Area (km)", value=kmaera, inline=True)
    embedVar.add_field(name="Capital", value=ccaptial, inline=False)
    embedVar.add_field(name="Population", value=popu, inline=True)
    embedVar.add_field(name="Wikipedia", value=wikiarticle, inline=False)
    print("DOUBLE STATS")
    #await ctx.send(embed=embedVar)

stats()
